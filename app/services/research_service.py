import json

from app.llm.llm_service import llm_service
from app.schemas.research import ResearchReport
from app.prompts.system_prompts import (
    RESEARCH_REPORT_PROMPT,
)
from app.utils.json_parser import parse_json
from app.utils.logger import logger


class ResearchService:

    def research(self, topic: str, search_results: str) -> ResearchReport:

        logger.info(f"Starting research for topic: {topic}")

        prompt = f"""
        Research Topic:
        {topic}

        Search Results:
        {search_results}
        """

        response = llm_service.ask_json(
            question=prompt,
            system_prompt=RESEARCH_REPORT_PROMPT,
            temperature=0.1
        )

        try:

            logger.info("Parsing LLM response")

            data = parse_json(response)

            logger.info("JSON parsed successfully")

            report = ResearchReport(**data)

            logger.info("Research report validated")

            return report

        except Exception as e:

            logger.error(f"Failed to create report: {e}")

            raise


research_service = ResearchService()