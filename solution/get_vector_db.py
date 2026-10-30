# get_vector_db.py - Vector Database verbinding (OPLOSSING)

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from config import CHROMA_PATH, COLLECTION_NAME, TEXT_EMBEDDING_MODEL


def get_vector_db():
    """
    Maakt verbinding met ChromaDB en retourneert een Chroma vector database.

    De collectie wordt automatisch aangemaakt als ze nog niet bestaat.
    """
    embeddings = OllamaEmbeddings(model=TEXT_EMBEDDING_MODEL)

    db = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
    )

    return db
