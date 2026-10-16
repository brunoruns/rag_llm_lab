# chroma_tester.py - Snel testen of ChromaDB werkt
#
# Gebruik:  python vector_database/chroma_tester.py
#
# Deze test gebruikt een persistente client, net zoals in het labo.
# De data wordt bewaard in ./chroma_test (wordt genegeerd door git).

import chromadb

# Persistente client: data overleeft herstarts van het script
chroma_client = chromadb.PersistentClient(path="./chroma_test")

# get_or_create_collection: geen fout als de collectie al bestaat
collection = chroma_client.get_or_create_collection(name="my_collection")

collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["This is a query document about hawaii"],  # Chroma embedt dit voor je
    n_results=2,  # hoeveel resultaten terug te geven
)
print(results)
