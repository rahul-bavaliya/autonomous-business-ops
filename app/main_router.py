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

from app.utils.logger import logger


def main():

    while True:
    
    
        logger.info(
            "Router Application Started"
        )

        question = input(
            "Question: "
        )

        route = router_agent.route(
            question
        )

        if route == "knowledge":

            answer = knowledge_agent.answer(
                question
            )

            print("\nKNOWLEDGE AGENT\n")
            print(answer)

        else:

            search_context = search_tool.search(
                question
            )

            report = research_service.research(
                topic=question,
                search_results=search_context
            )

            print("\nRESEARCH AGENT\n")

            print(
                f"\nTITLE\n{report.title}\n"
            )

            print(
                f"\nSUMMARY\n{report.summary}\n"
            )

        if question.lower() == "exit":
            break   


if __name__ == "__main__":

    main()