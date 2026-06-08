from app.utils.logger import logger


class Reranker:

    def rerank(
        self,
        query: str,
        context: str,
        top_k: int = 3
    ) -> str:

        logger.info(
            f"Reranking results for: {query}"
        )

        chunks = [
            chunk.strip()
            for chunk in context.split("\n\n")
            if chunk.strip()
        ]

        query_words = set(
            query.lower().split()
        )

        scored_chunks = []

        for chunk in chunks:

            chunk_words = set(
                chunk.lower().split()
            )

            score = len(
                query_words.intersection(
                    chunk_words
                )
            )

            scored_chunks.append(
                (
                    score,
                    chunk
                )
            )

        scored_chunks.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        best_chunks = [
            chunk
            for score, chunk
            in scored_chunks[:top_k]
        ]

        logger.info(
            f"Selected {len(best_chunks)} chunks"
        )

        return "\n\n".join(
            best_chunks
        )


reranker = Reranker()