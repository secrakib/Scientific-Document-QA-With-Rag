import sys, os
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_community.document_loaders.parsers import LLMImageBlobParser

def data_loader(path: str, extract_images: bool = False):
    
    if extract_images:
        gemini_flash = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            max_output_tokens=300,
            temperature=0.2
        )
        image_parser = LLMImageBlobParser(model=gemini_flash)
        loader = PyMuPDF4LLMLoader(
            file_path=path,
            table_strategy="lines",
            extract_images=True,
            images_parser=image_parser
        )
    else:
        loader = PyMuPDF4LLMLoader(
            file_path=path,
            table_strategy="lines",
            extract_images=False
        )
    
    docs = loader.load()
    return docs