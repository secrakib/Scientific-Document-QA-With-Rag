# 🔬 Context-Aware Scientific Document Q/A System  
*A Retrieval-Augmented Generation (RAG) system for interactive scientific document exploration.*

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://paperchat-frontend.onrender.com/)


<!-- Optional: Add a preview GIF or screenshot -->


[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)

---

## 📘 Overview

This project enables **natural language interaction with scientific PDFs**, allowing users to query documents conversationally and receive **context-aware, memory-driven** responses.

By combining **RAG techniques, Gemini embeddings, and FAISS semantic search**, the system delivers accurate, contextually grounded answers while maintaining conversational memory across interactions.

---

## 🚀 Key Features

- 🧠 **Context-Aware Q/A** — Understands user queries in the context of prior conversation.  
- 🔍 **Semantic Search with FAISS** — Retrieves the most relevant document chunks efficiently.  
- 🔗 **RAG Pipeline (LangChain)** — Connects retrieval, document, and memory chains for precise, dynamic reasoning.  
- 💬 **Interactive UI** — Built with Streamlit for seamless document upload and exploration.  
- ✅ **Tested & Modular Design** — Comprehensive unit tests across all core modules.  

---

## 🧩 Processing Pipeline

```
                          ┌───────────────────┐
                          │   User / Frontend │
                          │   (Streamlit UI) │
                          └─────────┬────────┘
                                    │ Upload PDF / Ask Query
                                    ▼
                          ┌───────────────────┐
                          │     Backend       │
                          │   (FastAPI API)   │
                          └─────────┬────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
 ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
 │ PDF Upload      │       │ Query / Session │       │ Session Memory  │
 │ (uploads/)      │       │ Validation      │       │ (memory_chain)  │
 └─────────┬───────┘       └─────────┬───────┘       └─────────┬───────┘
           │                         │                         │
           ▼                         ▼                         ▼
 ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
 │ PDF Loader      │       │ Text Splitter    │       │ Retriever        │
 │ data_loader()   │──────▶│ text_splitter() │──────▶│ retriver()       │
 └─────────┬───────┘       └─────────┬───────┘       └─────────┬───────┘
           │                         │                         │
           ▼                         ▼                         ▼
 ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
 │ Metadata        │       │ Embeddings       │       │ FAISS Vector DB  │
 │ ingestion       │       │ gemini_embedding │──────▶│ vector_database │
 └─────────┬───────┘       └─────────┬───────┘       └─────────┬───────┘
           │                         │                         │
           └──────────────┬──────────┴─────────────┬───────────┘
                          ▼                        ▼
                  ┌──────────────────────────┐
                  │ Document / Retrieval     │
                  │ Chains (RAG Pipeline)    │
                  │ document_chain(),        │
                  │ retrival_chain(),        │
                  │ memory_chain()           │
                  └─────────┬────────────────┘
                            │
                            ▼
                  ┌──────────────────────────┐
                  │ LLM Response             │
                  │ llm() generates answer   │
                  └─────────┬────────────────┘
                            │
                            ▼
                  ┌──────────────────────────┐
                  │ Frontend / User UI       │
                  │ Displays Answer          │
                  └──────────────────────────┘

```


---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **LLM Framework** | LangChain |
| **Embeddings** | Gemini |
| **Vector Store** | FAISS |
| **Backend API** | FastAPI |
| **Frontend** | Streamlit |
| **Deployment** | Render |

---

## 🧠 How It Works

1. **Upload a PDF** → The document is split into semantically meaningful chunks.  
2. **Embedding Generation** → Each chunk is embedded using **Gemini embeddings**.  
3. **FAISS Indexing** → Chunks are stored and retrieved efficiently via **FAISS**.  
4. **RAG Processing** → A **LangChain pipeline** retrieves relevant chunks and generates responses.  
5. **Conversational Memory** → User history is retained for context-aware answers.

---

## 🧑‍💻 Setup & Installation

### Clone and Run the Project
```
Clone the repo

git clone https://github.com/yourusername/context-aware-scientific-qa.git
cd context-aware-scientific-qa

Create a Virtual Environment

python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows

Install Dependencies
pip install -r requirements.txt

4. Run the Streamlit App
streamlit run app.py
```

### 🔧 Environment Variables
This project requires a .env file in the root directory to store environment-specific configuration values.
Create a file named .env in the project root with the following content:
```
# .env
GOOGLE_API_KEY=your_google_api_key_here
```

### 📚 Example Query
```
User: “What is the main contribution of this paper?”
System: “The paper proposes a context-aware retrieval model for improved document-level question answering, leveraging multi-hop reasoning across sections.”
```

### 🧱 Project Structure
```
├─ .vscode/
│
├─ backend/
│  ├─ api/
│  │  ├─ uploads/
│  │  ├─ main.py
│  │  └─ __init__.py
│  │
│  ├─ chains/
│  ├─ embeddings/
│  ├─ ingestion/
│  ├─ llm/
│  ├─ retriever/
│  ├─ splitting/
│  ├─ vector_database/
│  ├─ Dockerfile
│  ├─ __init__.py
│  └─ requirements.txt
│
├─ frontend/
│  ├─ Dockerfile
│  ├─ __init__.py
│  ├─ app.py
│  └─ requirements.txt
│
├─ tests/
│
├─ uploads/
│
├─ .gitignore
├─ LICENSE
├─ README.md
├─ __init__.py
├─ docker-compose.yml
└─ requirements.txt

```
### ⚠️ Known Issues / Limitations
```
The system currently requires a Google API key to function; other API providers are not yet supported.

The embedding process may be slow for very large documents.

Frontend performance can degrade with large datasets.

Docker setup assumes a Unix-like environment; Windows users may need additional configuration.

Error handling and logging are minimal and should be improved for production use.

```
### 📈 Future Improvements
```
🔄 Support for multi-document context

🗣️ Voice query integration

🧩 Improved memory persistence with vectorized history

🌍 Support for multilingual scientific texts
```
### 

### 📄 License
```
This project is licensed under the MIT License
```
