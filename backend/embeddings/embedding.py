import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


#os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["GOOGLE_API_KEY"]=os.getenv('GOOGLE_API_KEY')



def embedding():
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    
    )
    return embeddings




