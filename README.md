# 🔬 Context-Aware Scientific Document Q/A System  (Python 3.12.4)
*A Retrieval-Augmented Generation (RAG) system for interactive scientific document exploration.*

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://paperchat-frontend.onrender.com/)


<!-- Optional: Add a preview GIF or screenshot -->


[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)

---

## 📘 Overview

This project enables **natural language interaction with scientific PDFs**, allowing users to query documents conversationally and receive **context-aware, memory-driven** responses.

By combining **RAG techniques, Gemini embeddings, and FAISS semantic search**, the system delivers accurate, contextually grounded answers while maintaining conversational memory across interactions.

---
---
### 💻 Application UI

<a href="https://github.com/user-attachments/assets/80200359-dee9-43ce-89db-598b4b4b4713">
  <img src="https://github.com/user-attachments/assets/80200359-dee9-43ce-89db-598b4b4b4713" width="600" alt="Screenshot 266"/>
</a>
<a href="https://github.com/user-attachments/assets/2f9d447b-0b10-481a-ba56-bf0a032c15c9">
  <img src="https://github.com/user-attachments/assets/2f9d447b-0b10-481a-ba56-bf0a032c15c9" width="600" alt="Screenshot 269"/>
</a>
<a href="https://github.com/user-attachments/assets/35a7413a-19a9-43c2-831f-0499b6a113a9">
  <img src="https://github.com/user-attachments/assets/35a7413a-19a9-43c2-831f-0499b6a113a9" width="600" alt="Screenshot 270"/>
</a>
<a href="https://github.com/user-attachments/assets/91c108c9-6cbe-4bde-8970-2e0735b5b5de">
  <img src="https://github.com/user-attachments/assets/91c108c9-6cbe-4bde-8970-2e0735b5b5de" width="600" alt="Screenshot 271"/>
</a>
<a href="https://github.com/user-attachments/assets/95070424-5494-40f8-8cb5-c56551e4a661">
  <img src="https://github.com/user-attachments/assets/95070424-5494-40f8-8cb5-c56551e4a661" width="600" alt="Screenshot 272"/>
</a>
<a href="https://github.com/user-attachments/assets/3c5b4d1a-0718-4a3f-ba6f-f1f33b462771">
  <img src="https://github.com/user-attachments/assets/3c5b4d1a-0718-4a3f-ba6f-f1f33b462771" width="600" alt="Screenshot 273"/>
</a>
<a href="https://github.com/user-attachments/assets/dd61bf10-5d61-4b6c-b55d-b038def0fe73">
  <img src="https://github.com/user-attachments/assets/dd61bf10-5d61-4b6c-b55d-b038def0fe73" width="600" alt="Screenshot 274"/>
</a>

---

## 🚀 Key Features

- 🧠 **Context-Aware Q/A** — Understands user queries in the context of prior conversation.  
- 🔍 **Semantic Search with FAISS** — Retrieves the most relevant document chunks efficiently.  
- 🔗 **RAG Pipeline (LangChain)** — Connects retrieval, document, and memory chains for precise, dynamic reasoning.  
- 💬 **Interactive UI** — Built with Streamlit for seamless document upload and exploration.
- 📊 Figure & Table Understanding — Can describe figures, extract and summarize tables, and answer queries related to tabular data for deeper document insights. 
- ✅ **Tested & Modular Design** — Comprehensive unit tests across all core modules.

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
| **Containerization** | Docker |
| **Pdf Extraction** | PyMuPDF4LLM |


---

## 🧑‍💻 Setup & Installation


Follow these steps to set up and run the project locally:

#### 1. Clone the Repository
```bash
git clone https://github.com/secrakib/Scientific-Pdf-Rag.git
cd Scientific-Pdf-Rag
```
### 2. Create a Virtual Environment
```
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
### 3. Install Python Dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
### 4. Install Docker (if not already installed)
### 5. Build and Run Docker Containers
```
docker compose build
docker compose up
```

## 🔧 Environment Variables
This project requires a .env file in the root directory to store environment-specific configuration values.
Create a file named .env in the project root with the following content:
```
# .env
GOOGLE_API_KEY=your_google_api_key_here
```

## 📚 Example Query
```
User: “What is the main contribution of this paper?”
System: “The paper proposes a novel Multimodal dataset for bengali hate speech.”
```

## 🧱 Project Structure
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
## ⚠️ Known Issues / Limitations

- 🔑 **Google API Dependency** — Currently requires a Google API key; other embedding providers are not yet supported.  
- 🐢 **Slow  on Large Documents** — Processing can be time-consuming for very large files.  
- 🧾 **Limited Error Handling & Logging** — Needs more robust error reporting and logging for production environments.  
- 🖼️ **Figure Description Timing** — Figure descriptions are generated during document loading, so direct queries about figures may yield limited results.  
- 📉 **Parsing Challenges** — Complex research papers may have figures or tables that the parser fails to extract or interpret correctly.  
- 🤖 **Adaptive but Inconsistent Behavior** — The model may initially fail to answer some queries but improve when the same question is re-asked later in the conversation.
- 🖥️ Live Demo Performance — The live demo may be slow due to limited resources on Render Free.



### 📄 License
```
This project is licensed under the MIT License
```
