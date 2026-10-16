#!/usr/bin/env bash
#
# Devcontainer setup voor het RAG LLM Labo.
#
# - Start Ollama (alleen als het nog niet draait)
# - Wacht tot de Ollama API klaar is
# - Pull de benodigde modellen (idempotent: alleen als ze ontbreken)
#
# Dit script is idempotent en draait bij elke containerstart,
# dus een tweede start is altijd snel.

set -euo pipefail

OLLAMA_URL="http://127.0.0.1:11434"

# --- 1. Start Ollama (eenmalig) -------------------------------------------
if ! pgrep -x ollama >/dev/null 2>&1; then
    echo "▶ Starten van Ollama-server..."
    nohup ollama serve >/tmp/ollama.log 2>&1 &
else
    echo "✅ Ollama draait al."
fi

# --- 2. Wacht tot de Ollama API bereikbaar is -----------------------------
echo "⏳ Wachten tot Ollama klaar is..."
ready=0
for _ in $(seq 1 60); do
    if curl -fsS "${OLLAMA_URL}/api/tags" >/dev/null 2>&1; then
        ready=1
        break
    fi
    sleep 1
done

if [ "$ready" -ne 1 ]; then
    echo "❌ Ollama werd niet klaar binnen 60s. Check /tmp/ollama.log" >&2
    exit 1
fi
echo "✅ Ollama is klaar."

# --- 3. Pull modellen (idempotent) ----------------------------------------
pull_model() {
    local model="$1"
    if ollama list | awk '{print $1}' | grep -qx "$model"; then
        echo "✅ Model al aanwezig: $model"
    else
        echo "⬇️  Downloaden van model: $model (kan enkele minuten duren)..."
        ollama pull "$model"
        echo "✅ Model klaar: $model"
    fi
}

# Embeddings-model (verplicht voor ChromaDB)
pull_model "nomic-embed-text"

# LLM-model voor tekstgeneratie. Overschrijf met: LLM_MODEL=llama3.2:1b bash scripts/devcontainer-setup.sh
# (of pas LLM_MODEL aan in opgave/.env). Op machines zonder GPU is "llama3.2:1b" sneller.
pull_model "${LLM_MODEL:-llama3.2:3b}"

echo ""
echo "🎉 Setup klaar. Overzicht van beschikbare modellen:"
ollama list
