import chromadb

from app.utils.logger import logger


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="knowledge_base"
            )
        )

    def add_document(
        self,
        doc_id: str,
        text: str,
        embedding: list[float]
    ):

        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding]
        )

        logger.info(
            f"Added document: {doc_id}"
        )

    def search(
        self,
        embedding: list[float],
        top_k: int = 3
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )


vector_store = VectorStore()