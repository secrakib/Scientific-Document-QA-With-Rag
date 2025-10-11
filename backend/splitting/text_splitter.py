import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


from langchain_text_splitters import RecursiveCharacterTextSplitter
def text_splitter(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2500,chunk_overlap=350)
    splitted_text = text_splitter.split_documents(docs)
    return splitted_text
