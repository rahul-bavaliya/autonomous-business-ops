from app.agents.executive_agent import (
    executive_agent
)

from app.agents.planner_agent import (
    planner_agent
)

from app.workflows.planner_workflow import (
    planner_workflow
)

from app.utils.logger import logger


class ExecutiveWorkflow:

    def run(
        self,
        goal: str
    ):

        logger.info(
            f"CEO Goal Received: {goal}"
        )

        # =====================
        # CREATE MISSION
        # =====================

        mission = executive_agent.create_mission(
            goal
        )

        print("\nMISSION\n")
        print(mission.model_dump_json(
            indent=4
        ))

        # =====================
        # CREATE PLAN
        # =====================

        plan = planner_agent.create_plan(
            mission.goal
        )

        print("\nPLAN\n")

        for step in plan.steps:

            print(
                f"{step.step_id}. "
                f"{step.agent} -> "
                f"{step.action}"
            )

        # =====================
        # EXECUTE PLAN
        # =====================

        report = planner_workflow.run(
            mission.goal
        )

        return report


executive_workflow = ExecutiveWorkflow()