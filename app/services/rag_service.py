from urllib import response

from app.agents.query_rewriter import (
    query_rewriter
)

from app.rag.hybrid_retriever import (
    hybrid_retriever
)

from app.llm.llm_service import (
    llm_service
)

from app.rerank.reranker import reranker
from app.utils.logger import (
    logger
)


class RAGService:

    def answer(
        self,
        question: str,
        history: list
    ) ->  dict:

        logger.info(
            f"RAG question received: {question}"
        )

        history = history or []

        # Rewrite query using conversation history
        rewritten_question = query_rewriter.rewrite(
            question=question,
            history=history
        )

        logger.info(f"Original Question: {question}")

        logger.info(f"Rewritten Question: {rewritten_question}")

        # Hybrid Retrieval
        context = hybrid_retriever.retrieve(
            rewritten_question
        )

        if len(context) < 150:
            logger.info("Insufficient context. Escalating to Research Agent.")
            return "__NEED_RESEARCH__"

        context = reranker.rerank(
            query=rewritten_question,
            context=context
        )

        logger.info(
            f"Reranked Context : "
            f"{(context)}"
        )

        # Build conversation history text
        history_text = ""

        for message in history:

            history_text += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )

        prompt = f"""
You are a helpful AI assistant.

Conversation History:
{history_text}

Knowledge Base Context:
{context}

Current User Question:
{question}

Instructions:

1. Use the Knowledge Base Context first.
2. Use Conversation History to resolve references:
   - it
   - they
   - this
   - that
   - he
   - she
3. Prefer facts found in the context.
4. If information is missing, clearly say:
   "I could not find that information in the knowledge base."
5. Do not invent facts.
6. Keep answers concise but complete.

Answer:
"""

        response = llm_service.ask(
            question=prompt,
            system_prompt=(
                "You are a helpful AI assistant "
                "specialized in retrieval augmented generation."
            ),
            temperature=0.2
        )

        return {
            "answer": response,
            "context": context,
            "context_length": len(context)
        }


rag_service = RAGService()