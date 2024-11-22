# pull ollama models
echo 'running setup-ollama.sh'
ollama serve
ollama pull mistral
ollama pull nomic-embed-text

# setup done.