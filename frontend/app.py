import time
import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import streamlit as st
import requests
import os


API_URL = os.getenv("API_URL", "http://localhost:8000")

API_URL = API_URL.rstrip('/')

st.set_page_config(
    page_title="PDF Q&A Assistant",
    page_icon="📄",
    layout="centered"
)


if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "filename" not in st.session_state:
    st.session_state.filename = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.title("📄 PDF Q&A Assistant")
st.markdown("Upload a PDF and ask questions about its content")

with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        if st.button("Process PDF", type="primary"):
            with st.spinner("Processing PDF..."):
                try:
                    # Upload file to API
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                    response = requests.post(f"{API_URL}/upload", files=files)
                    
                    if response.status_code == 200:
                        data = response.json()
                        st.session_state.session_id = data["session_id"]
                        st.session_state.filename = data["filename"]
                        st.session_state.chat_history = []
                        st.success(f"✅ {data['message']}")
                        st.rerun()
                    else:
                        st.error(f"❌ Error: {response.json().get('detail', 'Unknown error')}")
                except Exception as e:
                    st.error(f"❌ Connection error: {str(e)}")
    
    
    if st.session_state.session_id:
        st.divider()
        st.success(f"**Active Session**")
        st.info(f"📄 **File:** {st.session_state.filename}")
        
        if st.button("Clear Session", type="secondary"):
            try:
                requests.delete(f"{API_URL}/session/{st.session_state.session_id}")
            except:
                pass
            st.session_state.session_id = None
            st.session_state.filename = None
            st.session_state.chat_history = []
            st.rerun()


if st.session_state.session_id is None:
    st.info("👈 Please upload a PDF file from the sidebar to get started")
else:
    
    st.markdown("### 💬 Conversation")
    
    
    chat_container = st.container()
    
    with chat_container:
        if len(st.session_state.chat_history) == 0:
            st.markdown("*No questions asked yet. Start by asking a question below.*")
        else:
            for i, qa in enumerate(st.session_state.chat_history):
                
                with st.chat_message("user"):
                    st.markdown(f"**Query:** {qa['query']}")
                
                
                with st.chat_message("assistant"):
                    st.markdown(f"**Answer:** {qa['answer']}")
    
    st.divider()
    
    
    with st.form(key="query_form", clear_on_submit=True):
        query = st.text_input(
            "Ask a question about your PDF:",
            placeholder="e.g., What is the main topic of this document?",
            key="query_input"
        )
        submit_button = st.form_submit_button("Submit", type="primary")
        
        if submit_button:
            if not query or query.strip() == "":
                st.warning("⚠️ Query cannot be empty. Please enter a valid question.")
            elif len(query) > 1000:
                st.warning("⚠️ Query is too long. Please limit to 1000 characters.")
            else:
                with st.spinner("Generating answer..."):
                    try:
                        
                        payload = {
                            "session_id": st.session_state.session_id,
                            "query": query
                        }
                        response = requests.post(f"{API_URL}/query", json=payload)
                        
                        if response.status_code == 200:
                            data = response.json()
                            
                            st.session_state.chat_history.append({
                                "query": query,
                                "answer": data["answer"]
                            })
                            st.rerun()
                        else:
                            error_detail = response.json().get('detail', 'Unknown error')
                            st.error(f"❌ {error_detail}")
                    except requests.exceptions.ConnectionError:
                        st.error("❌ Cannot connect to API. Please ensure the backend is running.")
                    except Exception as e:
                        st.error(f"❌ Sorry, I couldn't generate an answer. Please try again.")


st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Powered by LangChain & FastAPI</div>",
    unsafe_allow_html=True
)

