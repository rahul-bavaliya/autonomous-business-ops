import json

from app.llm.llm_service import llm_service
from app.schemas.plan import Plan
from app.utils.logger import logger


class PlannerAgent:

    def create_plan(
        self,
        goal: str
    ) -> Plan:

        logger.info(
            f"Creating plan for: {goal}"
        )

        prompt = f"""
    You are an expert AI Planner Agent.

    Your job is to break a user's goal into
    a sequence of executable steps.

    Each step must contain:

    - step_id
    - agent
    - action

    Available Agents:

    1. ResearchAgent
    - internet research
    - market research
    - competitor analysis

    2. KnowledgeAgent
    - company knowledge base
    - RAG retrieval
    - internal documents

    3. AnalysisAgent
    - compare information
    - rank results
    - summarize findings

    Return ONLY valid JSON.

    Example:

    {{
    "goal": "Find AI Engineer jobs in Saskatchewan",
    "steps": [
        {{
        "step_id": 1,
        "agent": "ResearchAgent",
        "action": "Find Saskatchewan companies hiring AI Engineers"
        }},
        {{
        "step_id": 2,
        "agent": "ResearchAgent",
        "action": "Collect salary and requirements"
        }},
        {{
        "step_id": 3,
        "agent": "AnalysisAgent",
        "action": "Rank jobs by relevance"
        }}
    ]
    }}

    User Goal:
    {goal}
    """

        response = llm_service.ask_json(
            question=prompt,
            system_prompt="You are a planning agent.",
            temperature=0
        )

        logger.info(
            f"Plan generated: {response}"
        )

        data = json.loads(response)

        # Backward compatibility
        if "tasks" in data and "steps" not in data:

            data["steps"] = []

            for i, task in enumerate(
                data["tasks"],
                start=1
            ):

                data["steps"].append(
                    {
                        "step_id": i,
                        "agent": "ResearchAgent",
                        "action": task
                    }
                )

            del data["tasks"]

        return Plan(**data)


planner_agent = PlannerAgent()