from app.workflows.planner_workflow import (
    planner_workflow
)


goal = input(
    "Goal: "
)

result = planner_workflow.run(
    goal
)

print("\nFINAL REPORT\n")

print(result)