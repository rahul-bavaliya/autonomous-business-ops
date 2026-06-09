from app.agents.planner_agent import (
    planner_agent
)

from app.agents.analysis_agent import (
    analysis_agent
)

from app.schemas import plan
from app.tools.search_tool import (
    search_tool
)

from app.services.research_service import (
    research_service
)

from app.utils.logger import logger


class PlannerWorkflow:

    def run(
        self,
        goal: str
    ):

        logger.info(
            f"Starting workflow for: {goal}"
        )

        plan = planner_agent.create_plan(
            goal
        )

        print("\nPLAN\n")
        
        logger.info(f"{plan}")
        
        # for step in plan.steps:

        #     print(
        #         f"{step.step_id}. "
        #         f"{step.agent} -> "
        #         f"{step.action}"
        #     )

        research_results = []

        for step in plan.steps:

            # ==================
            # RESEARCH AGENT
            # ==================
            if step.agent == "ResearchAgent":

                logger.info(
                    f"Executing: {step.action}"
                )

                search_context = (
                    search_tool.search(
                        step.action
                    )
                )

                report = (
                    research_service.research(
                        topic=step.action,
                        search_results=search_context
                    )
                )

                research_results.append(
                    f"""
Title:
{report.title}

Summary:
{report.summary}
"""
                )

            # ==================
            # ANALYSIS AGENT
            # ==================
            elif step.agent == "AnalysisAgent":

                logger.info(
                    "Running analysis"
                )

                final_report = (
                    analysis_agent.analyze(
                        goal=goal,
                        research_results=research_results
                    )
                )

                return final_report

        return "Workflow completed."


planner_workflow = PlannerWorkflow()