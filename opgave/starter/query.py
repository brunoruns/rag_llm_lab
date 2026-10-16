# query.py - Vragen stellen aan je documenten
#
# Dit is het hart van de RAG pipeline:
# 1. Ontvang een vraag van de gebruiker
# 2. Zoek relevante context in de vector database
# 3. Stuur de context + vraag naar het LLM
# 4. Geef het antwoord terug
#
# 💡 Vraag aan je AI assistant:
#    "Wat is een RAG chain precies? Leg de pijplijn uit van
#     retriever → prompt → llm → output parser."

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_classic.retrievers import MultiQueryRetriever
from config import LLM_MODEL
from get_vector_db import get_vector_db


def get_prompt():
    """
    Maakt de prompt templates voor de RAG chain.

    QUERY_PROMPT: instrueren hoe het LLM queries moet herformuleren
    prompt: het sjabloon voor context + vraag → antwoord
    """
    QUERY_PROMPT = PromptTemplate(
        input_variables=["question"],
        template="""Je bent een assistent die documenten doorzoekt.
        Genereer 3 verschillende zoekopdrachten voor de volgende vraag.
        Original question: {question}""",
    )

    template = """Beantwoord de vraag uitsluitend op basis van de volgende context.
    Als het antwoord niet in de context staat, zeg dan dat je het niet weet.

    Context:
    {context}

    Vraag: {question}

    Antwoord:"""

    prompt = ChatPromptTemplate.from_template(template)
    return QUERY_PROMPT, prompt


def query(input_text):
    """
    Hoofdfunctie: verwerk een natuurlijke vraag en retourneer een antwoord.

    Gebruikt MultiQueryRetriever om meerdere zoekvarianten te genereren,
    haalt relevante chunks op uit ChromaDB, en laat de LLM een antwoord
    formuleren op basis van de gevonden context.
    """
    if not input_text:
        return None

    # TODO: Initialiseer de LLM

    # TODO: Haal de vector database op

    # TODO: Haal de prompt templates op

    # TODO: Maak een MultiQueryRetriever

    # TODO: Bouw de RAG chain

    # TODO: Voer de chain uit en retourneer het antwoord

    return None  # Vervang door echte implementatie
