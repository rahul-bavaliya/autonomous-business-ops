from app.agents.router_agent import (
    router_agent
)

from app.agents.knowledge_agent import (
    knowledge_agent
)

from app.tools.search_tool import (
    search_tool
)

from app.services.research_service import (
    research_service
)

from app.memory.memory_manager import (
    memory
)

from app.agents.query_rewriter import (
    query_rewriter
)

from app.utils.logger import logger


def main():

    while True:

        logger.info(
            "Router Application Started"
        )

        question = input(
            "Question: "
        )

        if question.lower() == "exit":
            break

        route = router_agent.route(
            question
        )

        # ==========================
        # KNOWLEDGE AGENT
        # ==========================
        if route == "knowledge":

            result = knowledge_agent.answer(
                question
            )

            answer = result["answer"]
            context = result["context"]

            knowledge_failed = (
                "could not find" in answer.lower()
                or "not in the knowledge base" in answer.lower()
            )

            # --------------------------
            # FALLBACK TO RESEARCH
            # --------------------------
            if knowledge_failed:

                logger.info(
                    "Knowledge base failed. Falling back to Research Agent."
                )

                history = memory.get_history()

                rewritten_question = query_rewriter.rewrite(
                    question=question,
                    history=history
                )

                logger.info(
                    f"Fallback Research Query: {rewritten_question}"
                )

                search_context = search_tool.search(
                    rewritten_question
                )

                report = research_service.research(
                    topic=rewritten_question,
                    search_results=search_context
                )

                # SAVE FALLBACK RESPONSE TO MEMORY
                memory.add_user_message(
                    question
                )

                memory.add_assistant_message(
                    f"{report.title}\n\n{report.summary}"
                )

                print(
                    "\nRESEARCH AGENT (FALLBACK)\n"
                )

                print(
                    f"\nTITLE\n{report.title}\n"
                )

                print(
                    f"\nSUMMARY\n{report.summary}\n"
                )

            # --------------------------
            # KNOWLEDGE SUCCESS
            # --------------------------
            else:

                # SAVE KNOWLEDGE RESPONSE TO MEMORY
                memory.add_user_message(
                    question
                )

                memory.add_assistant_message(
                    answer
                )

                print(
                    "\nKNOWLEDGE AGENT\n"
                )

                print(
                    answer
                )

        # ==========================
        # RESEARCH AGENT
        # ==========================
        else:

            history = memory.get_history()

            rewritten_question = query_rewriter.rewrite(
                question=question,
                history=history
            )

            logger.info(
                f"Research Query: {rewritten_question}"
            )

            search_context = search_tool.search(
                rewritten_question
            )

            report = research_service.research(
                topic=rewritten_question,
                search_results=search_context
            )

            memory.add_user_message(
                question
            )

            memory.add_assistant_message(
                f"{report.title}\n\n{report.summary}"
            )

            print(
                "\nRESEARCH AGENT\n"
            )

            print(
                f"\nTITLE\n{report.title}\n"
            )

            print(
                f"\nSUMMARY\n{report.summary}\n"
            )


if __name__ == "__main__":

    main()