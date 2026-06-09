from pydantic import BaseModel


class Mission(BaseModel):

    goal: str

    mission_type: str

    priority: str

    required_agents: list[str]