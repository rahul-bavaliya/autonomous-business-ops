from app.utils.logger import logger


SEARCH_KEYWORDS = [
    "latest",
    "today",
    "current",
    "news",
    "recent",
    "stock",
    "weather",
    "price",
    "earnings",
    "update"
]


class RouterAgent:

    def route(
        self,
        question: str
    ) -> str:

        logger.info(f"Routing question: {question}")

        question_lower = question.lower()

        for keyword in SEARCH_KEYWORDS:

            if keyword in question_lower:

                logger.info(
                    "Route: research"
                )

                return "research"

        logger.info(
            "Route: knowledge"
        )

        return "knowledge"


router_agent = RouterAgent()