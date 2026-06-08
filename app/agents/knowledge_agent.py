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
    ) -> str:

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

        memory.add_user_message(
            question
        )

        memory.add_assistant_message(
            response
        )

        return response


knowledge_agent = KnowledgeAgent()