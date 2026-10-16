# Use Python 3.12 as base
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install system dependencies for document processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    zstd \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama (local LLM runner) - idempotent
RUN if ! command -v ollama >/dev/null 2>&1; then \
        curl -fsSL https://ollama.com/install.sh | sh; \
    fi

# Install uv (fast Python package manager)
RUN pip install --no-cache-dir uv

# Create workspace directory
WORKDIR /workspace

# Copy the dependency manifest first for better layer caching,
# then install everything from the single source of truth (pyproject.toml)
COPY pyproject.toml README.md ./
RUN uv pip install --system -e '.[dev]'

# Expose ports: 5000 = Flask app, 11434 = Ollama API
EXPOSE 5000 11434
