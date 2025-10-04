import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.llm.llm import llm
from backend.embeddings.embedding import gemini_embedding
from backend.vector_database.vector_database import faiss_vector_database
from backend.splitting.text_splitter import text_splitter
from backend.ingestion.pdf_loader import data_loader
from backend.retriver.retriver import retriver
from backend.chains.document_chain import document_chain
from backend.chains.retrival_chain import retrival_chain
from backend.retriver.history_aware_retriver import history_retriver
from langchain_community.chat_message_histories import ChatMessageHistory
from backend.chains.memory_chain import memory_chain,get_session_history
from langchain_core.documents import Document

path = 'backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf'
loaded_docs = data_loader(path)

# Split documents
splitted_docs = text_splitter(loaded_docs)
'''# Create test documents
splitted_docs = [
    Document(page_content="The capital of France is Paris."),
    Document(page_content="The population of Paris is about 2.2 million.")
]'''
# Create vector database
embedding = gemini_embedding()
vector_database = faiss_vector_database(splitted_docs, embedding)

# Setup LLM and retriever
llm_model = llm()
retriever_instance = retriver(vector_database)
history_aware_retriever = history_retriver(llm_model, retriever_instance)

# Create chains
doc_chain = document_chain(llm_model)
retrieval_chain_instance = retrival_chain(history_aware_retriever, doc_chain)

memory_chain= memory_chain(retrieval_chain_instance)


# Test conversation with memory
session_id = "test_session_3"

# First question
response1 = memory_chain.invoke(
    {"input": "What is the title of the paper?"},
    config={"configurable": {"session_id": session_id}}
)
print("Q1:", response1["answer"])

# Follow-up question (tests memory)
response2 = memory_chain.invoke(
    {"input": "What language is mentioned in your previous answer?"},
    config={"configurable": {"session_id": session_id}}
)
print("\nQ2:", response2["answer"])
print()
print()
print(response2)
history = get_session_history(session_id)
print("\n \n")
print("\nChat History Messages:", len(history.messages))
print(history.messages)


'''chat_history = ChatMessageHistory()
chat_history.add_user_message("Sylhet is famous for Tea.")
chat_history.add_ai_message("Ok.Thank you for the knowledge.")

response= retrieval_chain_instance.invoke({
    "input": "Why Sylhet is famous for?",
    "chat_history": chat_history.messages
})

print(response['answer'])
print(response)'''

