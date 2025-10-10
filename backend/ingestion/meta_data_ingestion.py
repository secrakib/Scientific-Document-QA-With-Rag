import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List, Optional
import json


class PaperMetadata(BaseModel):
    """Structured output model for research paper metadata."""
    title: str = Field(description="The title of the research paper")
    author: str = Field(description="The authors of the paper (comma-separated if multiple)")
    subject: str = Field(description="The abstract or subject/summary of the paper")
    keywords: str = Field(default="", description="Keywords or index terms (comma-separated)")


def metadata_extraction(document: List, google_api_key: str, model: str = "gemini-2.5-pro") -> List:
    """
    Extract metadata from the first document and apply it to all documents.
    
    Args:
        document: List of LangChain Document objects from PDF loader
        google_api_key: Your Google API key for Gemini
        model: Gemini model to use (default: gemini-2.0-flash-exp)
    
    Returns:
        None as the original object is modified in this function
    """
    if not document:
        print("No documents provided.")
        return document
    
    # Check first document for missing metadata
    first_doc = document[0]
    missing_fields = []
    
    for field in ["title", "author", "subject", "keywords"]:
        if not first_doc.metadata.get(field):
            missing_fields.append(field)
    
    # If no fields are missing, return as is
    if not missing_fields:
        print(" All metadata already exists; no LLM call needed.")
        return document
    
    print(f" Missing fields detected: {missing_fields}")
    print(" Extracting metadata from first document...")
    
    # Initialize LLM with structured output
    llm = ChatGoogleGenerativeAI(
        model=model,
        google_api_key=google_api_key,
        temperature=0
    )
    
    # Use structured output with Pydantic model
    structured_llm = llm.with_structured_output(PaperMetadata)
    
    # Get content from first document (limit to avoid token overflow)
    text_content = first_doc.page_content[:8000]
    
    # Create prompt
    prompt_template = PromptTemplate(
        input_variables=["content"],
        template=(
            "You are an expert at extracting metadata from research papers. "
            "Analyze the document text below and extract:\n\n"
            "1. Title - The full title of the paper\n"
            "2. Authors - All authors (comma-separated)\n"
            "3. Subject - The abstract or main subject/summary\n"
            "4. Keywords - Index terms or keywords (comma-separated, or empty if not found)\n\n"
            "Document text:\n{content}\n\n"
            "Extract the metadata accurately."
        )
    )
    
    prompt = prompt_template.format(content=text_content)
    
    try:
        # Get structured output
        extracted_metadata = structured_llm.invoke(prompt)
        
        # Convert to dict
        metadata_dict = {
            "title": extracted_metadata.title,
            "author": extracted_metadata.author,
            "subject": extracted_metadata.subject,
            "keywords": extracted_metadata.keywords
        }
        
        print(" Metadata extracted successfully:")
        print(f"   Title: {metadata_dict['title'][:60]}...")
        print(f"   Author: {metadata_dict['author'][:60]}...")
        print(f"   Keywords: {metadata_dict['keywords'][:60] if metadata_dict['keywords'] else 'None'}")
        
    except Exception as e:
        print(f" Error during extraction: {e}")
        print("Using fallback empty metadata.")
        metadata_dict = {
            "title": "",
            "author": "",
            "subject": "",
            "keywords": ""
        }
    
    # Apply extracted metadata to ALL documents
    print(f"\n Applying metadata to all {len(document)} documents...")
    
    for doc in document:
        for key in ["title", "author", "subject", "keywords"]:
            if not doc.metadata.get(key):
                doc.metadata[key] = metadata_dict[key]
    
    print(" Metadata successfully applied to all documents!")
    
    return doc


