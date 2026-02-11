import subprocess
import time
import sys
import os

def start_services():
    print("🚀 Starting DiaClassifier Full Stack...")
    
    # 1. Start FastAPI Backend
    print("📦 Launching FastAPI Backend (Port 8000)...")
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "api.main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Wait for backend to be ready
    time.sleep(3)
    
    # 2. Start Streamlit Frontend
    print("🎨 Launching Streamlit Frontend (Port 8501)...")
    frontend_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "app/main.py", "--server.port", "8501"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    print("\n✅ Both services are running!")
    print("👉 API Documentation: http://127.0.0.1:8000/docs")
    print("👉 Streamlit Dashboard: http://127.0.0.1:8501")
    print("\nPress Ctrl+C to stop all services.")
    
    try:
        while True:
            # Optionally print output from processes
            line = backend_process.stdout.readline()
            if line:
                pass # print(f"[Backend] {line.strip()}")
            
            line = frontend_process.stdout.readline()
            if line:
                pass # print(f"[Frontend] {line.strip()}")
                
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping services...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Done.")

if __name__ == "__main__":
    start_services()
