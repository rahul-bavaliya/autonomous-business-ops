from app.llm.llm_service import llm_service
from app.utils.logger import logger


class QueryRewriter:

    def rewrite(
        self,
        question: str,
        history: list = None
    ) -> str:

        logger.info(
            "Rewriting query"
        )

        history_text = ""

        if history:

            for message in history[-6:]:

                history_text += (
                    f"{message['role']}: "
                    f"{message['content']}\n"
                )

        prompt = f"""
Conversation History:
{history_text}

Current Question:
{question}

Rewrite the question so it is fully self-contained.

Examples:

What is LangGraph?
Who created it?

→ Who created LangGraph?

Only return the rewritten question.
"""

        rewritten = llm_service.ask(
            question=prompt,
            system_prompt=(
                "You rewrite search queries."
            ),
            temperature=0
        )

        logger.info(
            f"Rewritten query: {rewritten}"
        )

        return rewritten.strip()


query_rewriter = QueryRewriter()