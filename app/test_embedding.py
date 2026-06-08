from app.embeddings.embedding_service import (
    embedding_service
)

embedding = embedding_service.embed(
    "LangGraph is an agent framework"
)

print(
    f"Dimensions: {len(embedding)}"
)

print(
    embedding[:10]
)