import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain

def document_chain(llm):
    
    qa_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a specialized research paper assistant. Your role is to provide accurate, evidence-based answers derived strictly from the provided research paper content.

    IMPORTANT GUIDELINES:
    - ONLY answer questions that can be directly addressed using the provided context below
    - If a question falls outside the scope of the provided context, politely inform the user that the information is not available in the current research paper
    - Cite specific sections or findings from the context when answering
    - If the context is insufficient to fully answer a question, acknowledge the limitations
    - Maintain academic rigor and precision in your responses
    - When relevant, reference previous parts of the conversation to maintain continuity

    CONTEXT FROM RESEARCH PAPER:
    {context}

    If the user's question cannot be answered using the above context, respond with: "I apologize, but I cannot find information about that topic in the provided research paper. I can only answer questions based on the content available in this document. Would you like to ask something else related to this research?"
    """),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}")
    ])
    

    
    stuff_documents_chain = create_stuff_documents_chain(llm, qa_prompt)

    return stuff_documents_chain





