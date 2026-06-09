from app.workflows.executive_workflow import (
    executive_workflow
)

goal = input(
    "CEO Goal: "
)

report = executive_workflow.run(
    goal
)

print(report)