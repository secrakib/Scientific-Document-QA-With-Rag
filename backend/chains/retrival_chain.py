import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain.chains import create_retrieval_chain

def retrival_chain(retriver,document_chain):
    chain = create_retrieval_chain(
        retriver,
        document_chain
    )
    return chain

