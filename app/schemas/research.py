from pydantic import BaseModel
from typing import List


class ResearchReport(BaseModel):
    title: str
    summary: str
    key_points: List[str]
    recommendations: List[str]