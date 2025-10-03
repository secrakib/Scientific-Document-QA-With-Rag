import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


def history_retriver(llm,retriver):
    history_prompt = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            ("human", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm, retriver, history_prompt
    )

    return history_aware_retriever
