# app.py - Webserver (Flask)
#
# Dit is het toegangspunt voor de gebruiker.
# Start deze server en communicier via HTTP.
#
# Routes:
#   POST /embed  → Upload een PDF-document
#   POST /query  → Stel een vraag over je documenten
#
# 💡 Vraag aan je AI assistant:
#    "Hoe werken POST routes in Flask? Wat is het verschil
#     tussen request.json en request.files?"

from flask import Flask, request, jsonify
from embed import embed
from query import query

app = Flask(__name__)


@app.route('/embed', methods=['POST'])
def embed_route():
    """
    Ontvang een PDF, sla de embeddings op in ChromaDB.
    Verwacht: multipart/form-data met een 'file' veld.
    """
    # TODO: Controleer of er een bestand is meegezonden

    return jsonify({"error": "Not implemented yet"}), 501


@app.route('/query', methods=['POST'])
def query_route():
    """
    Ontvang een vraag, retourneer een antwoord op basis van
    de documenten in de vector database.
    Verwacht: JSON met {'question': '...'}
    """
    # TODO: Haal de vraag uit de JSON body

    return jsonify({"error": "Not implemented yet"}), 501


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
