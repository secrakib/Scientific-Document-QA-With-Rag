import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.llm.llm import llm
llm=llm()
response = llm.invoke('What is the capital of bangladesh?')
print(response)