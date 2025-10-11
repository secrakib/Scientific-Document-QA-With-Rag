from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import shutil
import uuid
from typing import Optional
import sys

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from llm.llm import llm
from embeddings.embedding import gemini_embedding
from vector_database.vector_database import faiss_vector_database
from splitting.text_splitter import text_splitter
from ingestion.pdf_loader_V2 import data_loader
from ingestion.meta_data_ingestion import metadata_ingested_docs
from retriver.retriver import retriver
from chains.document_chain import document_chain
from chains.retrival_chain import retrival_chain
from retriver.history_aware_retriver import history_retriver
from chains.memory_chain import memory_chain, get_session_history

app = FastAPI(title="RAG PDF Query API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Storage for active sessions
sessions = {}
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

class QueryRequest(BaseModel):
    session_id: str
    query: str

class QueryResponse(BaseModel):
    answer: str
    session_id: str

class UploadResponse(BaseModel):
    session_id: str
    filename: str
    message: str

@app.get("/")
async def root():
    return {"message": "RAG PDF Query API is running"}

@app.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """Upload and process a PDF file"""
    try:
        # Validate file type
        if not file.filename.endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")
        
        # Generate session ID
        session_id = str(uuid.uuid4())
        
        # Save uploaded file
        file_path = UPLOAD_DIR / f"{session_id}_{file.filename}"
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process PDF
        loaded_docs = data_loader(str(file_path),extract_images=True)
        docs_with_metadata=metadata_ingested_docs(loaded_docs,'gemini-2.5-flash-lite')
        splitted_docs = text_splitter(docs_with_metadata)
        
        # Create vector database
        embedding = gemini_embedding()
        vector_database = faiss_vector_database(splitted_docs, embedding)
        
        # Setup LLM and retriever
        llm_model = llm()
        retriever_instance = retriver(vector_database)
        history_aware_retriever = history_retriver(llm_model, retriever_instance)
        
        # Create chains
        doc_chain = document_chain(llm_model)
        retrieval_chain_instance = retrival_chain(history_aware_retriever, doc_chain)
        mem_chain = memory_chain(retrieval_chain_instance)
        
        # Store session
        sessions[session_id] = {
            "memory_chain": mem_chain,
            "filename": file.filename,
            "file_path": str(file_path)
        }
        
        return UploadResponse(
            session_id=session_id,
            filename=file.filename,
            message="PDF uploaded and processed successfully"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

@app.post("/query", response_model=QueryResponse)
async def query_pdf(request: QueryRequest):
    """Query the uploaded PDF"""
    try:
        # Validate query
        if not request.query or request.query.strip() == "":
            raise HTTPException(status_code=400, detail="Query cannot be empty. Please enter a valid question.")
        
        if len(request.query) > 1000:
            raise HTTPException(status_code=400, detail="Query is too long. Please limit to 1000 characters.")
        
        # Check if session exists
        if request.session_id not in sessions:
            raise HTTPException(status_code=404, detail="Session not found. Please upload a PDF first.")
        
        # Get memory chain for this session
        mem_chain = sessions[request.session_id]["memory_chain"]
        
        # Query the chain
        response = mem_chain.invoke(
            {"input": request.query},
            config={"configurable": {"session_id": request.session_id}}
        )
        
        return QueryResponse(
            answer=response["answer"],
            session_id=request.session_id
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail="Sorry, I couldn't generate an answer. Please try again."
        )

@app.get("/session/{session_id}")
async def get_session_info(session_id: str):
    """Get session information"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    history = get_session_history(session_id)
    
    return {
        "session_id": session_id,
        "filename": sessions[session_id]["filename"],
        "message_count": len(history.messages)
    }

@app.delete("/session/{session_id}")
async def delete_session(session_id: str):
    """Delete a session and cleanup resources"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Delete uploaded file
    file_path = Path(sessions[session_id]["file_path"])
    if file_path.exists():
        file_path.unlink()
    
    # Remove session
    del sessions[session_id]
    
    return {"message": "Session deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)