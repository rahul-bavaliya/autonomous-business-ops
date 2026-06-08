from app.llm.llm_service import llm_service
from app.utils.logger import logger


class QueryRewriter:

    def rewrite(
        self,
        question: str,
        history: list
    ) -> str:

        logger.info("Rewriting query")

        if not history:
            return question

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

Task:
Rewrite the current question so it is completely self-contained.

Rules:
- Resolve pronouns such as:
  - it
  - its
  - they
  - them
  - their
  - this
  - that
  - those
  - these
- Use the conversation history to determine what the user is referring to.
- Preserve the original meaning.
- If the question is already self-contained, return it unchanged.
- Return ONLY the rewritten question.
- Do not explain your reasoning.

Examples:

Conversation:
User: What is LangGraph?
User: Who created it?

Output:
Who created LangGraph?

Conversation:
User: What is Saskatchewan?
User: What is its population?

Output:
What is the population of Saskatchewan?

Conversation:
User: Tell me about OpenAI.
User: When was it founded?

Output:
When was OpenAI founded?

Conversation:
User: What is Python?
User: How is it used in AI?

Output:
How is Python used in AI?

Current Question:
{question}
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