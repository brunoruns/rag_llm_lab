"""Smoke tests voor het RAG-lab.

Belangrijk: deze tests mogen slagen terwijl de TODO's nog NIET zijn
ingevuld. Ze verifiëren dat de starter-modules importeerbaar zijn en
dat het notebook geldig is en gegenereerd kan worden.
"""

from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parent.parent


def test_starter_modules_importable():
    import app  # noqa: F401
    import config  # noqa: F401
    import embed  # noqa: F401
    import get_vector_db  # noqa: F401
    import query  # noqa: F401


def test_config_reads_env_or_defaults():
    import config

    assert config.LLM_MODEL
    assert config.TEXT_EMBEDDING_MODEL


def test_get_vector_db_is_callable():
    import get_vector_db

    assert callable(get_vector_db.get_vector_db)


def test_query_is_callable():
    import query

    assert callable(query.query)
    # TODO's zijn nog niet ingevuld: lege input geeft gewoon None
    assert query.query("") is None


def test_notebook_exists_and_is_valid():
    nb_path = ROOT / "opgave" / "Opgave oefenlabo.ipynb"
    assert nb_path.exists(), "Genereer eerst het notebook: python tools/generate_notebook.py"

    nb = nbformat.read(nb_path, as_version=4)
    nbformat.validate(nb)
    assert len(nb.cells) >= 10
