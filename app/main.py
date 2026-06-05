from app.workflows.research_graph import (
    research_graph
)
from app.utils.logger import logger


def main():

    logger.info(
        "Application started"
    )

    topic = input(
        "Research Topic: "
    )

    logger.info(
        f"Running graph for topic: {topic}"
    )

    result = research_graph.invoke(
        {
            "topic": topic
        }
    )

    report = result["report"]

    print("\nTITLE")
    print(report["title"])

    print("\nSUMMARY")
    print(report["summary"])


if __name__ == "__main__":
    main()