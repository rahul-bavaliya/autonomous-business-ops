from app.rag.retriever import retriever
from app.rag.keyword_retriever import (
    keyword_retriever
)

from app.utils.logger import logger


class HybridRetriever:

    def retrieve(
        self,
        query: str
    ) -> str:

        logger.info(
            f"Hybrid retrieval for: {query}"
        )

        vector_context = retriever.retrieve(
            query
        )

        keyword_context = (
            keyword_retriever.retrieve(
                query
            )
        )

        combined_context = f"""
VECTOR SEARCH RESULTS
=====================

{vector_context}


KEYWORD SEARCH RESULTS
======================

{keyword_context}
"""

        logger.info(
            f"Hybrid context length: "
            f"{len(combined_context)}"
        )

        return combined_context


hybrid_retriever = HybridRetriever()