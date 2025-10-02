import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv()

os.environ["MISTRALAI_API_KEY"] = os.getenv("MISTRALAI_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


from langchain_mistralai import MistralAIEmbeddings
def embedding():
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=os.environ["MISTRALAI_API_KEY"]
    )
    return embeddings


