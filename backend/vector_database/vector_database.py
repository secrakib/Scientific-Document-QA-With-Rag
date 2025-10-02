import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain_community.vectorstores import Chroma
from backend.embeddings.embedding import embedding

def vector_database(docs,embedding):
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embedding
    )
    return vectorstore
