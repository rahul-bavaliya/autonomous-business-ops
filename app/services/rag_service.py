from app.rag.retriever import retriever
from app.llm.llm_service import llm_service
from app.utils.logger import logger
from app.agents.query_rewriter import (
    query_rewriter
)

class RAGService:

    def answer(
        self,
        question: str,
        history: list = None
    ) -> str:

        logger.info(
            f"Original Question: {question}"
        )

        

        rewritten_question = query_rewriter.rewrite(
            question=question,
            history=history
        )
        logger.info(
            f"Rewritten Question: {rewritten_question}"
        )
        context = retriever.retrieve(
            rewritten_question
        )

        history_text = ""

        if history:

            for message in history:

                history_text += (
                    f"{message['role']}: "
                    f"{message['content']}\n"
                )

        prompt = f"""
You are having a conversation with a user.

Conversation History:
{history_text}

Knowledge Base Context:
{context}

Current User Question:
{question}

Rules:
1. Use conversation history to resolve references such as:
   - it
   - they
   - that
   - this
2. Use the knowledge context when relevant.
3. If the user refers to something mentioned earlier, infer the reference from history.

Answer:
"""

        response = llm_service.ask(
            question=prompt,
            system_prompt=(
                "You are a helpful AI assistant."
            ),
            temperature=0.2
        )

        return response


rag_service = RAGService()