from app.services.research_service import (
    research_service
)

from app.memory.memory_manager import (
    memory
)

from app.utils.logger import logger


class ResearchAgent:

    def answer(
        self,
        question: str,
        search_context: str
    ):

        logger.info(
            "Research Agent selected"
        )

        report = research_service.research(
            topic=question,
            search_results=search_context
        )

        memory.add_user_message(
            question
        )

        memory.add_assistant_message(f"{report.title}\n\n{report.summary}")

        return report


research_agent = ResearchAgent()