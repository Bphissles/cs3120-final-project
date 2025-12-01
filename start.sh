#!/bin/bash
# Shamelessly generated with Google Gemini 3. 
# This was to make local development easier, not get better at bash scripting.
# Function to handle cleanup
cleanup() {
    echo ""
    echo "Shutting down services..."
    # Kill all child processes (background jobs)
    pkill -P $$
    exit
}

# Trap interrupts (Ctrl+C)
trap cleanup SIGINT SIGTERM

# Function to kill processes on specific ports
kill_port() {
    local port=$1
    local pid=$(lsof -ti tcp:$port)
    if [ -n "$pid" ]; then
        echo "Killing process on port $port (PID: $pid)..."
        kill -9 $pid
    fi
}

kill_existing() {
    echo "Checking for existing processes..."
    kill_port 5000 # Backend
    kill_port 3000 # Frontend
}

start_backend() {
    kill_port 5000
    echo "--- Starting Backend ---"
    cd backend || exit
    
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
        source venv/bin/activate
        if [ -f "requirements.txt" ]; then
            pip install -r requirements.txt
        fi
    else
        source venv/bin/activate
    fi

    # Run with unbuffered output
    PYTHONUNBUFFERED=1 python app.py &
    BACKEND_PID=$!
    cd ..
}

start_frontend() {
    kill_port 3000
    kill_port 3001
    echo "--- Starting Frontend ---"
    cd frontend || exit
    npm run dev &
    FRONTEND_PID=$!
    cd ..
}

# Command line arguments
if [ "$1" == "backend" ]; then
    start_backend
    wait $BACKEND_PID
elif [ "$1" == "frontend" ]; then
    start_frontend
    wait $FRONTEND_PID
else
    # Start both
    kill_existing
    start_backend
    start_frontend
    
    echo ""
    echo "------------------------------------------------"
    echo "Services are running!"
    echo "Backend API: http://127.0.0.1:5000/api"
    echo "Frontend:    http://localhost:3000"
    echo "------------------------------------------------"
    echo "Press Ctrl+C to stop all services."
    
    wait
fi
