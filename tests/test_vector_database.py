import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from langchain_community.vectorstores import Chroma
from backend.embeddings.embedding import embedding
from backend.ingestion.pdf_loader import data_loader
from backend.splitting.text_splitter import text_splitter
from backend.vector_database.vector_database import vector_database

loaded_docs = data_loader(r'backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf')
splitted_docs = text_splitter(loaded_docs)


embedding=embedding()

vector_database=vector_database(splitted_docs,embedding)
print(vector_database)
