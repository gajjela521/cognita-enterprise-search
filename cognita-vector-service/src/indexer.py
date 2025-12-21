import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../data')
INDEX_FILE = 'faiss_index.bin'
METADATA_FILE = 'metadata.pkl'
MODEL_NAME = 'all-MiniLM-L6-v2'

def load_documents(data_dir):
    documents = []
    if not os.path.exists(data_dir):
        print(f"Data directory {data_dir} does not exist.")
        return documents
        
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple chunking by line for this demo, or just paragraph
                # Ideally, you'd overlap, but let's keep it simple: split by newlines
                lines = [line.strip() for line in content.split('\n') if line.strip()]
                documents.extend(lines)
    return documents

def create_index(documents):
    if not documents:
        print("No documents to index.")
        return

    print(f"Loading model: {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    
    print(f"Encoding {len(documents)} documents...")
    embeddings = model.encode(documents)
    
    # FAISS expects float32
    embeddings = np.array(embeddings).astype('float32')
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    
    print("Building FAISS index...")
    index.add(embeddings)
    
    return index, model, embeddings

def save_system(index, documents):
    print(f"Saving index to {INDEX_FILE}...")
    faiss.write_index(index, INDEX_FILE)
    
    print(f"Saving metadata to {METADATA_FILE}...")
    with open(METADATA_FILE, 'wb') as f:
        pickle.dump(documents, f)
    print("Done.")

if __name__ == "__main__":
    print("Starting indexing process...")
    docs = load_documents(DATA_DIR)
    if docs:
        idx, _, _ = create_index(docs)
        save_system(idx, docs)
    else:
        print("No documents found in data directory.")
