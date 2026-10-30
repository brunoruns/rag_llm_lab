# query.py - Vragen stellen aan je documenten (OPLOSSING)

from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama
from config import LLM_MODEL
from get_vector_db import get_vector_db


def get_prompt():
    """Maakt de prompt templates voor de RAG chain."""
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
    """Verwerk een natuurlijke vraag en retourneer een antwoord."""
    if not input_text:
        return None

    llm = ChatOllama(model=LLM_MODEL)
    db = get_vector_db()
    QUERY_PROMPT, prompt = get_prompt()

    retriever = MultiQueryRetriever.from_llm(
        db.as_retriever(),
        llm,
        prompt=QUERY_PROMPT,
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    response = chain.invoke(input_text)
    return response
