
# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Install system-level dependencies, including distutils for setuptools
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libpng-dev \
    python3-distutils \
    && apt-get clean

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel cython

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
