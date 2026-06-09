import json

from app.llm.llm_service import (
    llm_service
)

from app.models.mission import (
    Mission
)

from app.utils.logger import (
    logger
)


class ExecutiveAgent:

    def create_mission(
        self,
        goal: str
    ) -> Mission:

        logger.info(
            f"Creating mission for: {goal}"
        )

        system_prompt = f"""
        You are a CEO Executive Agent.

        Analyze the CEO goal and determine:

        1. mission_type
        2. priority
        3. required_agents

        Available Agents:

        - ResearchAgent
        - KnowledgeAgent
        - AnalysisAgent
        - PlannerAgent

        Mission Types:

        - research
        - knowledge
        - business_analysis
        - job_search
        - travel_planning
        - project_management

        Priority:

        - low
        - medium
        - high

        Return ONLY valid JSON.

        Example:

        {{
            "goal": "Find AI Engineer jobs in Regina",
            "mission_type": "job_search",
            "priority": "high",
            "required_agents": [
                "PlannerAgent",
                "ResearchAgent",
                "AnalysisAgent"
            ]
        }}"""

        user_prompt = f"""
        CEO Goal:
        {goal}

        Return ONLY valid JSON.

        Schema:

        {{
            "goal": "{goal}",
            "mission_type": "job_search | research | analysis | business",
            "priority": "high | medium | low",
            "required_agents": [
                "PlannerAgent",
                "ResearchAgent",
                "KnowledgeAgent",
                "AnalysisAgent"
            ]
        }}

        Return JSON only.
        """

        response = llm_service.ask_json(
            question=user_prompt,
            system_prompt=system_prompt,
            temperature=0
        )

        logger.info(
            f"Response: {response}"
        )

        response_dict = json.loads(response)

        mission = Mission(**response_dict)

        logger.info(f"Mission created: {mission}")

        logger.info(
            f"Mission created: {mission.mission_type}"
        )

        return mission


executive_agent = ExecutiveAgent()