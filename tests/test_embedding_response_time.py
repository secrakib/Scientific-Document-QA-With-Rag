import time
import requests
import sys,os,types
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def diagnose_embeddings():
    from backend.embeddings.embedding import gemini_embedding
    import time
    
    embedding_fn = gemini_embedding()
    
    # Test embedding speed
    test_texts = [
        "This is a test sentence for embedding speed.",
        "Machine learning models like BERT are used for NLP.",
        "Sentiment analysis in Bengali language processing."
    ]
    
    print("Testing embedding speed...")
    start_time = time.time()
    
    # Test single embedding
    single_start = time.time()
    emb1 = embedding_fn.embed_query(test_texts[0])
    single_time = time.time() - single_start
    print(f"Single embedding time: {single_time:.2f}s")
    
    # Test batch embedding
    batch_start = time.time()
    emb_batch = embedding_fn.embed_documents(test_texts)
    batch_time = time.time() - batch_start
    print(f"Batch embedding time (3 docs): {batch_time:.2f}s")
    print(f"Embedding dimension: {len(emb1)}")
    
    return embedding_fn

print(diagnose_embeddings())