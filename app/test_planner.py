from app.agents.planner_agent import planner_agent


goal = input(
    "Goal: "
)

plan = planner_agent.create_plan(
    goal
)

print("\nPLAN\n")

print(
    f"Goal: {plan.goal}\n"
)

for step in plan.steps:

    print(
        f"\nStep {step.step_id}"
    )

    print(
        f"Agent : {step.agent}"
    )

    print(
        f"Action: {step.action}"
    )