# 🔬 Context-Aware Scientific Document Q/A System  
*A Retrieval-Augmented Generation (RAG) system for interactive scientific document exploration.*

![Demo](https://your-demo-gif-or-screenshot-link) <!-- Optional: Add a preview GIF or screenshot -->


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

## 🧩 Architecture

      ┌───────────────────────────────┐
      │        User Interface          │
      │       (Streamlit App)          │
      └──────────────┬────────────────┘
                     │
            Query & Context Input
                     │
      ┌──────────────▼────────────────┐
      │     LangChain RAG Pipeline     │
      │ (Retriever + Memory + QA Chain)│
      └──────────────┬────────────────┘
                     │
         FAISS Index Search (Gemini)
                     │
      ┌──────────────▼────────────────┐
      │     Scientific PDF Chunks      │
      │     (Preprocessed via OCR)     │
      └───────────────────────────────┘


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

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/context-aware-scientific-qa.git
cd context-aware-scientific-qa

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the Streamlit App
streamlit run app.py
```


📚 Example Query
```
User: “What is the main contribution of this paper?”
System: “The paper proposes a context-aware retrieval model for improved document-level question answering, leveraging multi-hop reasoning across sections.”
```

🧱 Project Structure
```
📂 context-aware-scientific-qa
├── app.py                  # Streamlit UI
├── backend/
│   ├── api.py              # FastAPI endpoints
│   ├── rag_pipeline.py     # LangChain pipeline
│   ├── retriever.py        # FAISS + Gemini retrieval
│   ├── memory.py           # Conversation memory handler
│   └── utils.py
├── tests/
│   ├── test_pipeline.py
│   └── test_retriever.py
├── requirements.txt
└── README.md
```

📈 Future Improvements
```
🔄 Support for multi-document context

🗣️ Voice query integration

🧩 Improved memory persistence with vectorized history

🌍 Support for multilingual scientific texts
```


📄 License
```
This project is licensed under the MIT License
```
