import time
import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from backend.llm.llm import llm
from backend.vector_database.vector_database import faiss_vector_database
from backend.retriver.retriver import retriver
from backend.embeddings.embedding import gemini_embedding
from backend.splitting.text_splitter import text_splitter
from backend.ingestion.pdf_loader import data_loader

# Load and process documents
print("Loading documents...")
start_time = time.time()
loaded_docs = data_loader(r'backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf')
print(f"Document loading took: {time.time() - start_time:.2f} seconds")

start_time = time.time()
splitted_docs = text_splitter(loaded_docs)
print(f"Text splitting took: {time.time() - start_time:.2f} seconds")

embedding = gemini_embedding()
vector_database = faiss_vector_database(splitted_docs, embedding)
llm = llm()
retriever_obj = retriver(vector_database)

def history_aware_retriever(llm, retriever):
    # Use a simpler, faster prompt
    history_prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        ("human", "Generate a concise search query based on the conversation.")
    ])

    return create_history_aware_retriever(llm, retriever, history_prompt)

# Create history-aware retriever
history_aware_retriever_chain = history_aware_retriever(llm, retriever_obj)

def diagnose_performance():
    print("\n" + "="*50)
    print("PERFORMANCE DIAGNOSIS")
    print("="*50)
    
    # Test 1: Direct vector search (bypass LLM)
    print("\n1. Testing direct vector search (no LLM):")
    start_time = time.time()
    try:
        direct_results = retriever_obj.get_relevant_documents("BERT models")
        direct_time = time.time() - start_time
        print(f"Direct search time: {direct_time:.2f} seconds")
        print(f"Documents retrieved: {len(direct_results)}")
    except Exception as e:
        print(f"Direct search failed: {e}")
    
    # Test 2: History-aware search with timing
    print("\n2. Testing history-aware retriever:")
    chat_history = []
    query = "What ML models are used?"
    
    start_time = time.time()
    try:
        result = history_aware_retriever_chain.invoke({
            "chat_history": chat_history,
            "input": query
        })
        total_time = time.time() - start_time
        print(f"History-aware search time: {total_time:.2f} seconds")
        print(f"Documents retrieved: {len(result)}")
        
        # If direct search was successful, we can compare
        if 'direct_time' in locals():
            llm_time = total_time - direct_time
            print(f"Estimated LLM processing time: {llm_time:.2f} seconds")
            
    except Exception as e:
        print(f"History-aware search failed: {e}")

# Optimized test function
def optimized_test():
    print("\n" + "="*50)
    print("OPTIMIZED TESTING")
    print("="*50)
    
    test_cases = [
        {
            "name": "Simple query, no history",
            "chat_history": [],
            "query": "What ML models are used?"
        },
        {
            "name": "Follow-up query",
            "chat_history": [
                HumanMessage(content="What models were used?"),
                AIMessage(content="The research used BERT and transformer models.")
            ],
            "query": "Which one performed best?"
        }
    ]
    
    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        print(f"Query: {test_case['query']}")
        
        start_time = time.time()
        try:
            result = history_aware_retriever_chain.invoke({
                "chat_history": test_case['chat_history'],
                "input": test_case['query']
            })
            elapsed = time.time() - start_time
            
            print(f"Time: {elapsed:.2f} seconds")
            print(f"Documents: {len(result)}")
            
            if len(result) > 0:
                print(f"First doc preview: {result[0].page_content[:100]}...")
                
        except Exception as e:
            print(f"Error: {e}")

# Alternative: Use a simpler approach without history awareness for faster results
def simple_retriever_test():
    """Test using just the basic retriever for comparison"""
    print("\n" + "="*50)
    print("SIMPLE RETRIEVER TEST (No LLM, faster)")
    print("="*50)
    
    queries = [
        "machine learning models",
        "BERT transformer",
        "sentiment analysis",
        "research methodology"
    ]
    
    for query in queries:
        start_time = time.time()
        try:
            results = retriever_obj.get_relevant_documents(query)
            elapsed = time.time() - start_time
            print(f"Query: '{query}' - Time: {elapsed:.2f}s - Docs: {len(results)}")
        except Exception as e:
            print(f"Query: '{query}' - Error: {e}")

if __name__ == "__main__":
    diagnose_performance()
    optimized_test()
    simple_retriever_test()