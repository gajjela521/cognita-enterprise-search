# Local RAG Challenge

This project implements a local RAG system with 3 components:

1.  **Vector Service (Python/Flask)**: Handles text embedding and similarity search (FAISS).
2.  **API Gateway (Java/Spring Boot)**: Orchestrates requests and acts as the backend for the frontend.
3.  **Console (React/Vite)**: A beautiful UI for searching documents.

## Prerequisites

*   Python 3.10+
*   Java 17+
*   Node.js 18+

## Quick Start

### 1. Start Vector Service (The Brain)
```bash
cd cognita-vector-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the indexer to process data/sample.txt
python src/indexer.py

# Start the server (Port 5001)
python server.py
```

### 2. Start API Gateway (The Middleware)
```bash
cd cognita-api-gateway
./gradlew bootRun
# Runs on Port 8080
```

### 3. Start Frontend (The UI)
```bash
cd cognita-console
npm install
npm run dev
# Open http://localhost:5173
```

## Architecture
[React UI] -> [Spring Boot Gateway] -> [Python Vector Service] -> [FAISS Index]
