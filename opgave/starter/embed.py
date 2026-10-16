# embed.py - Documenten inladen, splitsen en opslaan
#
# Deze module verzorgt het volledige "ingest" proces:
# 1. Valideer het bestand (PDF)
# 2. Sla het tijdelijk op
# 3. Lees en split de inhoud in chunks
# 4. Sla de chunks op in de vector database
# 5. Ruim de tijdelijke bestanden op
#
# 💡 Vraag aan je AI assistant:
#    "Waarom splitsen we documenten in chunks voordat
#     we ze in de vector database opslaan? Wat is het
#     effect van chunk_size en chunk_overlap?"

import os
from datetime import datetime
from werkzeug.utils import secure_filename
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import TEMP_FOLDER
from get_vector_db import get_vector_db


def allowed_file(filename):
    """Controleert of het bestand een toegestaan type is (PDF)."""
    # TODO: implementeer deze functie
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}
    pass  # Vervang door echte implementatie


def save_file(file):
    """
    Slaat een geüpload bestand op in de tijdelijke folder.
    Gebruikt een timestamp om unieke bestandsnamen te maken.
    """
    # TODO: implementeer deze functie
    ct = datetime.now()
    ts = ct.timestamp()
    filename = str(ts) + "_" + secure_filename(file.filename)
    file_path = os.path.join(TEMP_FOLDER, filename)
    file.save(file_path)
    return file_path
    pass


def load_and_split_data(file_path):
    """
    Laadt een PDF in met PyMuPDFLoader en split de tekst
    in chunks met RecursiveCharacterTextSplitter.

    Experimenteer met chunk_size (500-2000) en chunk_overlap (50-200).
    Dit bepaalt hoe groot de tekstpassages zijn in de database.
    """
    # TODO: Laad het document
    loader = PyMuPDFLoader(file_path)
    data = loader.load()

    # TODO: Split de tekst in chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(data)
    return chunks
    pass


def embed(file):
    """
    Hoofdfunctie: valideer, sla op, split, sla op in DB en ruim op.

    Stappen:
    1. Check of de filename geldig is (allowed_file)
    2. Sla de file op (save_file)
    3. Laad in en split de data (load_and_split_data)
    4. Voeg chunks toe aan de vector database
    5. Verwijder het tijdelijke bestand
    """
    # TODO: implementeer embed functie
    if file and allowed_file(file.filename):
        # Sla het bestand op
        file_path = save_file(file)

        # Laad en split
        chunks = None
        # Voeg toe aan vector database

        # Genereer unieke IDs voor elke chunk

        # Opruimen

        return {"status": "success", "chunks": len(chunks)}
    return {"status": "error", "message": "Invalid file type"}
    pass
