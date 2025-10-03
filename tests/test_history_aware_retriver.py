import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate
from backend.llm.llm import llm
from backend.vector_database.vector_database import faiss_vector_database
from backend.retriver.retriver import retriver
from backend.embeddings.embedding import gemini_embedding
from backend.splitting.text_splitter import text_splitter
from backend.ingestion.pdf_loader import data_loader
from backend.retriver.history_aware_retriver import history_retriver
from langchain_core.messages import HumanMessage, AIMessage

loaded_docs = data_loader(r'backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf')
splitted_docs = text_splitter(loaded_docs)
embedding=gemini_embedding()
vector_database=faiss_vector_database(splitted_docs,embedding)
llm=llm()
retriver = retriver(vector_database)
history_aware_retriver=history_retriver(llm,retriver)

query = "Tell me more about these models"
chat_history = [
        HumanMessage(content="What ML models are used in the research?"),
        AIMessage(content="The research uses several ML models including BERT, DistilBERT, and other transformer models.")
    ]
result = history_aware_retriver.invoke({
            "chat_history": chat_history,
            "input": query
        })

print(result)
