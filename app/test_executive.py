from app.agents.executive_agent import (
    executive_agent
)


goal = input(
    "CEO Goal: "
)

mission = executive_agent.create_mission(
    goal
)

print("\nMISSION\n")

print(
    mission.model_dump_json(
        indent=4
    )
)