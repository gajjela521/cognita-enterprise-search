# Local RAG Challenge

A robust Retrieval Augmented Generation system with a multi-service architecture.

## Architecture

*   **Frontend**: React + TypeScript + Vite (Port 5173)
*   **Backend**: Spring Boot 3 (Port 8080)
*   **RAG Engine**: Python + Flask (Port 5000)

## Prerequisites

*   Java 17+
*   Node.js 18+
*   Python 3.9+

## Setup & Running

You need 3 terminal windows to run the full stack locally.

### 1. RAG Engine (Python)
This service handles the vector database (FAISS) and embeddings.

```bash
cd rag-engine
# Create virtual env (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

### 2. Backend API (Spring Boot)
This is the gateway that bridges the Frontend and the RAG Engine.

```bash
cd backend
./gradlew bootRun
```

### 3. Frontend (React)
The user interface.

```bash
cd frontend
npm install
npm run dev
```

Then open [http://localhost:5173](http://localhost:5173).

## Deployment

*   **Frontend**: Automatically deployed to GitHub Pages via GitHub Actions on push to `main`.
*   **Backend**: Currently configured for local development. For production, deploy the JAR to a cloud provider (Render, Railway, AWS, etc.).

## Project Structure

*   `/backend` - Spring Boot Application
*   `/frontend` - React Application
*   `/rag-engine` - Python FAISS/SentenceTransformer Logic
