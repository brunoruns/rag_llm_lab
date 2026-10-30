# 🎓 Oplossing (voor docenten)

Deze map bevat de **volledige, werkende oplossing** van het RAG-lab
(gerelateerd aan `opgave/starter/`). De oplossing is gemoderniseerd naar
**LangChain 1.x** en **ChromaDB 1.x**.

## Gebruik

Vervang de starter-bestanden door de oplossing:

```bash
# Vanuit de repository-root
cp solution/*.py opgave/starter/
```

Vereisten:
- Ollama draait (`ollama serve`)
- Modellen gepulled: `nomic-embed-text` en je gekozen `LLM_MODEL`
- `.env` aanwezig in `opgave/` (kopieer `opgave/.env.example`)

## Test

```bash
cd opgave
python starter/app.py            # start de Flask-server op poort 5000

# Upload een PDF
curl -X POST -F "file=@jouw_document.pdf" http://localhost:5000/embed

# Stel een vraag
curl -X POST -H "Content-Type: application/json" \
     -d '{"question":"Wat is de hoofdboodschap?"}' http://localhost:5000/query
```

## Nota over LangChain 1.x

- `MultiQueryRetriever` zit nu in het `langchain-classic` package:
  `from langchain_classic.retrievers import MultiQueryRetriever`
- Chroma-persistentie is automatisch: `db.persist()` bestaat niet meer.
- PDF-verwerking gebeurt met `PyMuPDFLoader` (licht, geen poppler nodig).
