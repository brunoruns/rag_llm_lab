# app.py - Webserver (Flask) (OPLOSSING)

import os

from flask import Flask, jsonify, request
from config import TEMP_FOLDER
from embed import embed
from query import query

os.makedirs(TEMP_FOLDER, exist_ok=True)

app = Flask(__name__)


@app.route('/embed', methods=['POST'])
def embed_route():
    """Ontvang een PDF en sla de embeddings op in ChromaDB."""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    result = embed(file)

    if result.get("status") == "success":
        return jsonify(result), 200
    return jsonify(result), 400


@app.route('/query', methods=['POST'])
def query_route():
    """Ontvang een vraag en retourneer een antwoord."""
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "No question provided"}), 400

    answer = query(data['question'])
    if answer:
        return jsonify({"answer": answer}), 200
    return jsonify({"error": "Something went wrong"}), 400


@app.route('/', methods=['GET'])
def home():
    """Welkomstpagina - test of de server draait."""
    return jsonify({
        "message": "RAG LLM Server draait!",
        "endpoints": {
            "POST /embed": "Upload een PDF-document",
            "POST /query": "Stel een vraag",
        }
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
