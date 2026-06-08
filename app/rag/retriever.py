from app.embeddings.embedding_service import (
    embedding_service
)

from app.embeddings.vector_store import (
    vector_store
)

from app.utils.logger import logger

class Retriever:
    def __init__(self):
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ):

        logger.info(
            f"Retrieving for query: {query}"
        )

        query_embedding = (
            self.embedding_service.embed(query)
        )

        results = (
            self.vector_store.search(
                embedding=query_embedding,
                top_k=top_k
            )
        )

        documents = results["documents"][0]

        return "\n\n".join(documents)


retriever = Retriever()