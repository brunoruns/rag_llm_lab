cd local-rag

# install chromadb
pip install --q chromadb

#install langchain tools
pip install --q unstructured langchain langchain-text-splitters
pip install --q "unstructured[all-docs]"
pip install --q langchain_community

#install flask
pip install --q flask

# pull ollama models
ollama pull mistral
ollama pull nomic-embed-text
ollama serve

# ollama serve ?

# setup done.