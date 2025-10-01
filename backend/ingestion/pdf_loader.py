import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))



from langchain_community.document_loaders import PDFMinerLoader
def data_loader(file_path):
    loader = PDFMinerLoader(file_path)
    docs = loader.load()
    return(docs)









