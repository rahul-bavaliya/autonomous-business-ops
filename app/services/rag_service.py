from app.rag.retriever import retrieve
from app.llm.llm_service import llm_service
from app.utils.logger import logger


class RAGService:

    def answer(
        self,
        question: str
    ) -> str:

        logger.info(
            f"RAG question received: {question}"
        )

        # Retrieve relevant context
        context = retrieve(
            query=question,
            top_k=3
        )

        logger.info(
            f"Retrieved context length: {len(context)}"
        )

        prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the context below.

If the answer is not present in the context, say:

"I could not find the answer in the knowledge base."

======================
CONTEXT
======================

{context}

======================
QUESTION
======================
"""

        response = llm_service.ask(
            question=question,
            system_prompt=prompt,
            temperature=0.2
        )

        logger.info(
            "RAG answer generated"
        )

        return response


rag_service = RAGService()