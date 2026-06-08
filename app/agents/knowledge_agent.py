from app.services.rag_service import (
    rag_service
)

from app.memory.memory_manager import (
    memory
)

from app.utils.logger import logger


class KnowledgeAgent:

    def answer(
        self,
        question: str
    ) -> dict:

        logger.info(
            "Knowledge Agent selected"
        )

        history = memory.get_history()

        print("\nMEMORY HISTORY")
        print(history)

        response = rag_service.answer(
            question=question,
            history=history
        )

        return {
            "answer": response["answer"],
            "context": response["context"],
            "context_length": response["context_length"]
        }


knowledge_agent = KnowledgeAgent()