# from chromadb import Client

# DB_DIR = "cv_chroma_db"

# client = Client(
#     persist_directory=DB_DIR
# )

# collection_name = "cv_job_summaries"

# def get_collection():
#     existing_collections = [c.name for c in client.list_collections()]
#     if collection_name in existing_collections:
#         return client.get_collection(collection_name)
#     return client.create_collection(collection_name)

# def add_text_to_vector_db(id: str, text: str):
#     collection = get_collection()
#     # Delete any existing document with same id to avoid duplicates
#     collection.delete(where={"ids": [id]})
#     collection.add(
#         documents=[text],
#         ids=[id],
#         metadatas=[{"source": id}]
#     )
#     client.persist()

# def search_similar_texts(text: str, n_results=5):
#     collection = get_collection()
#     results = collection.query(
#         query_texts=[text],
#         n_results=n_results,
#     )
#     return results
