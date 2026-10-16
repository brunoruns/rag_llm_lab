# config.py - Centrale configuratie voor het RAG Labo
# 
# Dit bestand laadt de omgevingsvariabelen uit .env
# en maakt ze beschikbaar voor de andere modules.
#
# 💡 Tip: Vraag aan je AI assistant:
#    "Leg uit hoe python-dotenv werkt en waarom we
#     omgevingsvariabelen gebruiken in plaats van
#     hardcoded waarden."

import os
from dotenv import load_dotenv

# Laad variabelen uit .env bestand
load_dotenv()

# Configuratie - wordt ingevuld vanuit .env of gebruikt standaardwaarden
TEMP_FOLDER = os.getenv('TEMP_FOLDER', './_temp')
CHROMA_PATH = os.getenv('CHROMA_PATH', 'chroma')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'local-rag')
LLM_MODEL = os.getenv('LLM_MODEL', 'llama3.2:3b')
TEXT_EMBEDDING_MODEL = os.getenv('TEXT_EMBEDDING_MODEL', 'nomic-embed-text')