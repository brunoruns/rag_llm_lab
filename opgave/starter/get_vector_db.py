# get_vector_db.py - Vector Database verbinding
#
# Deze module maakt verbinding met ChromaDB en geeft
# een Chroma-object terug waarin we documenten kunnen
# opslaan en opvragen.
#
# 💡 Wat is een vector database?
#    Vraag aan je AI assistant: "Leg in eenvoudige
#    bewoordingen uit wat een vector database is en
#    waarom we die nodig hebben voor RAG."

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from config import CHROMA_PATH, COLLECTION_NAME, TEXT_EMBEDDING_MODEL


def get_vector_db():
    """
    Maakt verbinding met ChromaDB en retourneert een Chroma vector database.

    Als de collectie nog niet bestaat, wordt deze automatisch aangemaakt.
    De embedding-functie zorgt ervoor dat teksten automatisch worden
    omgezet naar vectoren bij opslag en opvraging.
    """
    # TODO: Maak de embeddings met TEXT_EMBEDDING_MODEL

    # TODO: Maak de Chroma vector database, gebruikt de parameters uit config en de zojuist geïnitialiseerde embedding

    return db
    # pass  # Verwijder deze regel zodra je de TODO's hebt ingevuld
