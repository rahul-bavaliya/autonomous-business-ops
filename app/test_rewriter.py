from app.agents.query_rewriter import query_rewriter

history = [
    {
        "role": "user",
        "content": "What is LangGraph?"
    }
]

result = query_rewriter.rewrite(
    question="Who created it?",
    history=history
)

print(result)