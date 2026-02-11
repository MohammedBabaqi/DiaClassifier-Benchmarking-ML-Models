# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY api/ ./api/
COPY app/ ./app/
COPY model/ ./model/
COPY start_all.py .

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Environment variables
ENV API_URL=http://localhost:8000
ENV PYTHONUNBUFFERED=1

# Run the startup script
CMD ["python", "start_all.py"]
