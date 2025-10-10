import sys,os
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from langchain_community.document_loaders.parsers import LLMImageBlobParser

def data_loader(
    path: str,
    model: str = "gemini-2.5-flash-lite",
    extract_images: bool = False,
    max_output_tokens: int = 300,
    temperature: float = 0.2
):
    """
    Load PDF documents with optional image extraction.
    
    Args:
        file_path: Path to the PDF file
        model: Model name for Gemini
        extract_images: Whether to extract and parse images
        max_output_tokens: Maximum output tokens for the model
        temperature: Temperature setting for the model
    
    Returns:
        List of loaded documents
    """
    loader_kwargs = {
        "file_path": path,
        "table_strategy": "lines",
        "extract_images": extract_images
    }
    
    if extract_images:
        gemini_flash = ChatGoogleGenerativeAI(
            model=model,
            google_api_key= os.getenv("GOOGLE_API_KEY"),
            max_output_tokens=max_output_tokens,
            temperature=temperature
        )
        
        image_parser = LLMImageBlobParser(model=gemini_flash)
        loader_kwargs["images_parser"] = image_parser
    
    loader = PyMuPDF4LLMLoader(**loader_kwargs)
    docs = loader.load()
    
    return docs