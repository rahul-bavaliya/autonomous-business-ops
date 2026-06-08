from app.services.rag_service import rag_service
from app.utils.logger import logger


class KnowledgeAgent:

    def answer(
        self,
        question: str
    ) -> str:

        logger.info(
            "Knowledge Agent selected"
        )

        return rag_service.answer(
            question
        )


knowledge_agent = KnowledgeAgent()