from app.services.research_service import (
    research_service
)

from app.tools.search_tool import (
    search_tool
)

from app.tools.file_tool import (
    file_tool
)

from app.utils.logger import logger


class ResearchAgent:

    def run(self, topic: str):

        logger.info(
            f"Research Agent started: {topic}"
        )

        search_results = search_tool.search(
            topic
        )

        report = research_service.research(
            topic=topic,
            search_results=search_results
        )

        file_tool.save_json(
            filename=f"{topic.lower()}.json",
            data=report.model_dump()
        )

        logger.info(
            "Research Agent completed"
        )

        return report
    

    def answer(
        self,
        question: str,
        search_context: str
    ):

        logger.info("Research Agent selected")

        return research_service.research(
            topic=question,
            search_results=search_context
        )



research_agent = ResearchAgent()