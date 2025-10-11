import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))



from langchain_community.document_loaders import PyPDFLoader
def data_loader(file_path:str):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs









