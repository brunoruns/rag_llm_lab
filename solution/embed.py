# embed.py - Documenten inladen, splitsen en opslaan (OPLOSSING)

import os
from datetime import datetime

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from werkzeug.utils import secure_filename
from config import TEMP_FOLDER
from get_vector_db import get_vector_db


def allowed_file(filename):
    """Controleert of het bestand een toegestaan type is (PDF)."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}


def save_file(file):
    """Slaat een geüpload bestand op met een unieke (timestamp) naam."""
    ts = datetime.now().timestamp()
    filename = str(ts) + "_" + secure_filename(file.filename)
    file_path = os.path.join(TEMP_FOLDER, filename)
    file.save(file_path)
    return file_path


def load_and_split_data(file_path):
    """Laadt een PDF en split de tekst in chunks."""
    loader = PyMuPDFLoader(file_path)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(data)
    return chunks


def embed(file):
    """Valideer, sla op, split, sla op in DB en ruim op."""
    if file and allowed_file(file.filename):
        file_path = save_file(file)
        chunks = load_and_split_data(file_path)

        db = get_vector_db()
        chunk_ids = [f"{os.path.basename(file_path)}_{i}"
                     for i in range(len(chunks))]
        db.add_documents(documents=chunks, ids=chunk_ids)

        os.remove(file_path)
        return {"status": "success", "chunks": len(chunks)}

    return {"status": "error", "message": "Invalid file type"}
