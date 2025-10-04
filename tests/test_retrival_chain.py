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

path = 'backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf'
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

chat_history = ChatMessageHistory()
chat_history.add_user_message("Sylhet is famous for Tea.")
chat_history.add_ai_message("Ok.Thank you for the knowledge.")

response= retrieval_chain_instance.invoke({
    "input": "Why Sylhet is famous for? Use previous chats if you need to.",
    "chat_history": chat_history.messages
})

print(response['answer'])
print(response)