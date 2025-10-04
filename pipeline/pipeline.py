# main.py
import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.llm.llm import llm
from backend.vector_database.vector_database import faiss_vector_database
from backend.retriver.retriver import retriver
from backend.embeddings.embedding import gemini_embedding
from backend.splitting.text_splitter import text_splitter
from backend.ingestion.pdf_loader import data_loader
from backend.retriver.history_aware_retriver import history_retriver
from backend.chains.document_chain import document_chain
from backend.chains.retrival_chain import retrival_chain
from backend.chains.memory_chain import memory_chain, get_session_history

def pipeline(path:str,session_id,input:str):
    # Load PDF
    loaded_docs = data_loader(path)

    # Split documents
    splitted_docs = text_splitter(loaded_docs)

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

    # Add memory to chain
    conversational_chain = memory_chain(retrieval_chain_instance)

    result = conversational_chain.invoke(
    {"input": input},
    config={"configurable": {"session_id": session_id}}
    )

    return result



'''# If you want to use TRIMMER (keep only last 3 exchanges):
# Replace the get_session_history function call like this:

from langchain_core.runnables.history import RunnableWithMessageHistory

conversational_chain_with_trimmer = RunnableWithMessageHistory(
    retrieval_chain_instance,
    lambda session_id: get_trimmed_history(store, session_id),  # Use trimmer here
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# Now only last 3 message pairs will be remembered
result4 = conversational_chain_with_trimmer.invoke(
    {"input": "Summarize the paper"},
    config={"configurable": {"session_id": session_id}}
)
print(f"Answer 4 (with trimmer): {result4['answer']}")'''