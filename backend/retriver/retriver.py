import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


def retriver(vector_database):
    retriever = vector_database.as_retriever(search_kwargs={"k": 3})
    return retriever