from pathlib import Path

from app.utils.logger import logger


class KeywordRetriever:

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ) -> str:

        logger.info(
            f"Keyword retrieval for: {query}"
        )

        outputs_dir = Path("outputs")

        if not outputs_dir.exists():

            return ""

        query_words = {
            word.lower()
            for word in query.split()
            if len(word) > 2
        }

        matches = []

        for file in outputs_dir.glob("*.json"):

            try:

                content = file.read_text(
                    encoding="utf-8"
                )

                score = sum(
                    1
                    for word in query_words
                    if word in content.lower()
                )

                if score > 0:

                    matches.append(
                        (
                            score,
                            content[:1000]
                        )
                    )

            except Exception as ex:

                logger.error(
                    f"Failed reading {file}: {ex}"
                )

        matches.sort(
            key=lambda x: x[0],
            reverse=True
        )

        context = "\n\n".join(
            item[1]
            for item in matches[:top_k]
        )

        logger.info(
            f"Keyword matches found: {len(matches)}"
        )

        return context


keyword_retriever = KeywordRetriever()