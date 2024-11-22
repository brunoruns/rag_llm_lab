# Base image
FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set up environment
WORKDIR /workspace

# Ensure pip is up to date
RUN pip install --no-cache-dir --upgrade pip
