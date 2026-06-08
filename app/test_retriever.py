from app.rag.retriever import retrieve

context = retrieve(
    "What is LangGraph?"
)

print(context)