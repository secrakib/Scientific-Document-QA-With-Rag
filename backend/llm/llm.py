import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
from  langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

def llm():
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=.5,
        reasoning_effort="high"
    )
    return llm
