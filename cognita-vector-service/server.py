from flask import Flask, request, jsonify
from src.retriever import LocalRAG

app = Flask(__name__)

# Initialize RAG system once on startup
print("Initializing RAG system...")
rag_system = LocalRAG()
print("RAG system initialized.")

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400
    
    query_text = data['text']
    k = data.get('k', 3)
    
    try:
        results = rag_system.query(query_text, k=int(k))
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
