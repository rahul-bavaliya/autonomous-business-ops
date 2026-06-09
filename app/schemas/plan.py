from pydantic import BaseModel


class PlanStep(BaseModel):
    step_id: int
    agent: str
    action: str


class Plan(BaseModel):
    goal: str
    steps: list[PlanStep]