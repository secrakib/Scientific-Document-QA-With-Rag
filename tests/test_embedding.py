import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.embeddings.embedding import embedding
from backend.ingestion.pdf_loader import data_loader
from backend.splitting.text_splitter import text_splitter
embedding=embedding()



text = "LangChain is the framework for building context-aware reasoning applications"
text2 = "LangGraph is a library for building stateful, multi-actor applications with LLMs"
two_vectors = embedding.embed_documents([text, text2])

print(two_vectors)
print(len(two_vectors[0]))






