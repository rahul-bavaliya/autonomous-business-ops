from app.workflows.research_graph import (
    research_graph
)

result = research_graph.invoke(
    {
        "topic": "LangGraph"
    }
)

print(result)