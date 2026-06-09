from app.llm.llm_service import llm_service
from app.utils.logger import logger


class AnalysisAgent:

    def analyze(
        self,
        goal: str,
        research_results: list[str]
    ):

        logger.info(
            "Analysis Agent selected"
        )

        context = "\n\n".join(
            research_results
        )

        prompt = f"""
Goal:
{goal}

Research Results:
{context}

Analyze the research results and return ONLY valid JSON.

Required JSON format:

{{
    "goal": "original goal",
    "summary": "overall summary",
    "key_findings": [
        "finding 1",
        "finding 2",
        "finding 3"
    ],
    "recommendations": [
        "recommendation 1",
        "recommendation 2",
        "recommendation 3"
    ],
    "confidence": "High | Medium | Low"
}}

Rules:
- Return ONLY JSON.
- No markdown.
- No explanations outside JSON.
- key_findings must be an array of strings.
- recommendations must be an array of strings.
- confidence must be High, Medium, or Low.
"""

        report = llm_service.ask_json(
            question=prompt,
            system_prompt=(
                "You are an expert business analyst."
            ),
            temperature=0.2
        )

        return report


analysis_agent = AnalysisAgent()