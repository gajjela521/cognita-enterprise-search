import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
import sys

# Configuration
INDEX_FILE = 'faiss_index.bin'
METADATA_FILE = 'metadata.pkl'
MODEL_NAME = 'all-MiniLM-L6-v2'

class LocalRAG:
    def __init__(self):
        self.index = None
        self.documents = []
        self.model = None
        self.load_system()

    def load_system(self):
        try:
            print(f"Loading index from {INDEX_FILE}...")
            self.index = faiss.read_index(INDEX_FILE)
            
            print(f"Loading metadata from {METADATA_FILE}...")
            with open(METADATA_FILE, 'rb') as f:
                self.documents = pickle.load(f)
                
            print(f"Loading model: {MODEL_NAME}...")
            self.model = SentenceTransformer(MODEL_NAME)
        except Exception as e:
            print(f"Error loading system: {e}")
            print("Did you run indexer.py first?")
            sys.exit(1)

    def query(self, query_text, k=3):
        query_vector = self.model.encode([query_text])
        query_vector = np.array(query_vector).astype('float32')
        
        distances, indices = self.index.search(query_vector, k)
        
        results = []
        for i in range(k):
            idx = indices[0][i]
            dist = distances[0][i]
            if idx < len(self.documents):
                results.append({
                    "text": self.documents[idx],
                    "score": float(dist)
                })
        return results

if __name__ == "__main__":
    rag = LocalRAG()
    
    while True:
        user_query = input("\nEnter your query (or 'quit' to exit): ")
        if user_query.lower() in ['quit', 'exit']:
            break
            
        print(f"\nSearching for: '{user_query}'...")
        hits = rag.query(user_query)
        
        print("\nTop Results:")
        for i, hit in enumerate(hits):
            print(f"{i+1}. [Score: {hit['score']:.4f}] {hit['text']}")
