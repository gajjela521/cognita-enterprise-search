#!/bin/bash

# Function to kill background processes on exit
cleanup() {
    echo "Shutting down services..."
    kill $(jobs -p)
}
trap cleanup EXIT

echo "Starting Local RAG System..."

# 1. Start Vector Service
echo "Starting Vector Service (Port 5001)..."
cd cognita-vector-service
python3 -m venv venv
source venv/bin/activate
if [ ! -f faiss_index.bin ]; then
    echo "Index not found, running indexer..."
    python src/indexer.py
fi
python server.py &
VECTOR_PID=$!
cd ..

# 2. Start API Gateway
echo "Starting API Gateway (Port 8080)..."
cd cognita-api-gateway
./gradlew bootRun &
GATEWAY_PID=$!
cd ..

# 3. Start Frontend (React) - Commented out for Lightweight Mode
# echo "Starting Frontend (Port 5173)..."
# cd cognita-console
# npm install
# npm run dev &
# FRONTEND_PID=$!
# cd ..

echo "All services started!"
echo "Lightweight UI: http://localhost:8080/index.html"
echo "API Gateway: http://localhost:8080"
echo "Vector Service: http://localhost:5001"

wait $VECTOR_PID $GATEWAY_PID # $FRONTEND_PID
