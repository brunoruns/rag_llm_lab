# 🧠 RAG LLM Labo — Bouw je eigen chatbot met Retrieval Augmented Generation

Deze repository is gebaseerd op een tutorial en daarna aangepast met behulp van AI.

> **2-uur labo** | AP Hogeschool | Modern RAG met lokale LLMs

In dit labo bouw je een **eigen chatbot** die antwoorden kan geven op basis van **eigen documenten** (PDF). Geen cloud-abonnement, geen API-sleutel, geen internet nodig. Alles draait lokaal op je eigen machine.

---

## Snelle start (devcontainer — 1 klik)

Deze repository is klaar voor **GitHub Codespaces** of **VS Code DevContainer**:

1. Open deze repo in VS Code
2. Klik op "Reopen in Container" (of open in Codespaces)
3. Wacht tot de container klaar is (⏳ 2-3 min — de eerste start pullt ook de modellen)
4. Open de notebook in `opgave/` en begin!

Bij elke start draait `scripts/devcontainer-setup.sh` automatisch:

- start **Ollama** (als het nog niet draait)
- wacht tot Ollama klaar is
- pullt de modellen `nomic-embed-text` en `llama3.2:3b` (alleen als ze ontbreken)

> Geen GPU? Op GitHub Codespaces draait de LLM op de CPU. Gebruik dan het snellere, maar kleinere model:
> ```bash
> ollama pull llama3.2:1b
> ```
> en zet in `opgave/.env`: `LLM_MODEL = 'llama3.2:1b'`

---

## Lokale installatie

**Vereisten:** Python 3.12+ en [Ollama](https://ollama.com) geïnstalleerd.

```bash
# 1. Maak een virtuele omgeving
python -m venv venv
source venv/bin/activate          # Linux/Mac
# .\venv\Scripts\activate         # Windows

# 2. Installeer de benodigde packages (bron van waarheid: pyproject.toml)
pip install -r requirements.txt

# 3. Kopieer de configuratie
cd opgave
cp .env.example .env

# 4. Start Ollama (laat dit open in een aparte terminal)
ollama serve

# 5. Haal de modellen binnen (⏳ dit kan even duren)
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

Klaar! Open `opgave/Opgave oefenlabo.ipynb` in VS Code of Jupyter en volg de instructies.

---

## Projectstructuur

| Pad | Wat is het? |
|-----|-------------|
| `opgave/` | De notebook + alle bestanden voor het labo |
| `opgave/starter/` | Skelet-code — **jij vult de TODO's in!** |
| `opgave/.env.example` | Voorbeeldconfiguratie (kopieer naar `.env`) |
| `scripts/` | Setup-script voor de devcontainer (start Ollama + pull modellen) |
| `tests/` | Smoke tests (moeten slagen vóór en na het labo) |
| `solution/` | Volledige oplossing |
| `vector_database/` | Hulpscripts voor ChromaDB |
| `.devcontainer/` | Docker config voor devcontainer |
| `pyproject.toml` | Enige bron van waarheid voor dependencies |

---

## Hoe werkt het labo?

Het labo bestaat uit **4 delen** die je één voor één bouwt:

1. **Vector Database** — Zet ChromaDB op voor het opslaan van document chunks
2. **Embedding** — Laad een PDF in, splits in stukjes, en bewaar in de vector DB
3. **Query** — Stel een vraag, zoek relevante context, en genereer een antwoord met LLM
4. **Webserver** — Koppel alles aan een Flask API zodat je via HTTP kan communiceren

**AI-hulp**

Bij elke stap in de notebook staan 💡-tips met concrete vragen die je aan je AI assistant kunt stellen. Zo blijf je niet vastzitten.

---

## Modellen

| Model | Grootte | Best voor |
|-------|---------|-----------|
| `llama3.2:1b` | 1B | ⚡ Snelst op CPU (geen GPU) — aanrader in Codespaces |
| `llama3.2:3b` | 3B | ⚡ Snel, ideaal voor dit labo (standaard) |
| `phi4:3.8b` | 3.8B | 💪 Sterk antwoorden |

Je kiest het model in `opgave/.env`:

```ini
LLM_MODEL = 'llama3.2:3b'
```

---


### Installatie — troubleshooting

| Probleem | Oplossing |
|----------|-----------|
| `ollama` niet gevonden | Installeer [Ollama](https://ollama.com) |
| Import errors | Check `pip list`; controleer of je venv geactiveerd is |
| ChromaDB/Ollama connectie | Start Ollama eerst met `ollama serve` |
| Traag antwoord (geen GPU) | Gebruik `llama3.2:1b` i.p.v. `llama3.2:3b` |

### Ontwikkeling van dit labo

- **Notebook:** bewerk `tools/generate_notebook.py` en draai daarna
  `python tools/generate_notebook.py` (genereert + valideert `opgave/Opgave oefenlabo.ipynb`).
- **Testen:** `pip install -e ".[dev]"` en dan `python -m pytest tests/ -v`.
- **CI:** GitHub Actions bouwt de devcontainer en draait de tests bij elke PR.

---

## 📦 Dependencies

- [ChromaDB](https://www.trychroma.com/) — Vector database
- [LangChain](https://python.langchain.com/) 1.x — RAG framework
- [langchain-ollama](https://python.langchain.com/docs/integrations/llms/ollama/) — Ollama-integratie
- [Ollama](https://ollama.com/) — Lokale LLM runner
- [Flask](https://flask.palletsprojects.com/) — Webserver
- [PyMuPDF](https://pymupdf.readthedocs.io/) — PDF parsing (lichtgewicht)
