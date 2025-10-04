import time
import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.llm.llm import llm
from backend.chains.document_chain import document_chain
from langchain_core.documents import Document
from langchain_community.chat_message_histories import ChatMessageHistory

llm=llm()
document_chain=document_chain(llm)

docs = [
    Document(page_content="The Eiffle Tower is located in Paris, France. It was built in 1889."),
    Document(page_content="The tower is 330 meters tall and made of iron.")
]


chat_history = ChatMessageHistory()
chat_history.add_user_message("What's the height of Donald tower in America?")
chat_history.add_ai_message("It's height is same to Eiffle Tower")



response = document_chain.invoke({
    "input": "What's the Height of Donald Tower in America?",
    "context": docs,
    "chat_history": chat_history.messages
})

print(response)