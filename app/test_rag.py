from app.services.rag_service import (
    rag_service
)

question = input(
    "Question: "
)

answer = rag_service.answer(
    question
)

print("\nANSWER\n")
print(answer)