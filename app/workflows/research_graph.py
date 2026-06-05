from datetime import datetime
from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.services.research_service import research_service
from app.tools.file_tool import file_tool
from app.tools.search_tool import search_tool
from app.utils.logger import logger


class ResearchState(TypedDict, total=False):

    topic: str

    route: str

    search_results: str

    search_result_count: int

    search_quality: str

    report: dict


def router_node(
    state: ResearchState
):

    logger.info(
        "Running Router Node"
    )

    topic = state["topic"].lower()

    if (
        "today" in topic
        and "date" in topic
    ):

        logger.info(
            "Routing to Date Tool"
        )

        return {
            "route": "date"
        }

    logger.info(
        "Routing to Research Flow"
    )

    return {
        "route": "research"
    }


def route_query(
    state: ResearchState
):

    return state["route"]


def date_node(
    state: ResearchState
):

    logger.info(
        "Running Date Tool Node"
    )

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    report = {
        "title": "Today's Date",
        "summary": f"Today's date is {today}"
    }

    return {
        "report": report
    }


def search_node(
    state: ResearchState
):

    logger.info(
        "Running Search Node"
    )

    result = search_tool.search(
        state["topic"]
    )

    logger.info(
        f"Search result count: {result['result_count']}"
    )

    logger.info(
        f"Search result length: {len(result['search_results'])}"
    )

    return {
        "search_results": result[
            "search_results"
        ],
        "search_result_count": result[
            "result_count"
        ]
    }


def quality_check_node(
    state: ResearchState
):

    logger.info(
        "Running Quality Check Node"
    )

    count = state.get(
        "search_result_count",
        0
    )

    if count >= 3:

        logger.info(
            "Search quality is GOOD"
        )

        return {
            "search_quality": "good"
        }

    logger.warning(
        "Search quality is POOR"
    )

    return {
        "search_quality": "poor"
    }


def route_after_quality_check(
    state: ResearchState
):

    quality = state.get(
        "search_quality",
        "poor"
    )

    logger.info(
        f"Routing decision: {quality}"
    )

    if quality == "good":
        return "research"

    return "end"


def research_node(
    state: ResearchState
):

    logger.info(
        "Running Research Node"
    )

    report = research_service.research(
        topic=state["topic"],
        search_results=state[
            "search_results"
        ]
    )

    return {
        "report": report.model_dump()
    }


def save_node(
    state: ResearchState
):

    logger.info(
        "Running Save Node"
    )

    report = state["report"]

    filename = (
        "output_" +
        datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )
    )

    file_tool.save_json(
        filename=filename,
        data=report
    )

    return {}


graph_builder = StateGraph(
    ResearchState
)

graph_builder.add_node(
    "router",
    router_node
)

graph_builder.add_node(
    "date",
    date_node
)

graph_builder.add_node(
    "search",
    search_node
)

graph_builder.add_node(
    "quality_check",
    quality_check_node
)

graph_builder.add_node(
    "research",
    research_node
)

graph_builder.add_node(
    "save",
    save_node
)

graph_builder.add_edge(
    START,
    "router"
)

graph_builder.add_conditional_edges(
    "router",
    route_query,
    {
        "date": "date",
        "research": "search"
    }
)

graph_builder.add_edge(
    "date",
    "save"
)

graph_builder.add_edge(
    "search",
    "quality_check"
)

graph_builder.add_conditional_edges(
    "quality_check",
    route_after_quality_check,
    {
        "research": "research",
        "end": END
    }
)

graph_builder.add_edge(
    "research",
    "save"
)

graph_builder.add_edge(
    "save",
    END
)

research_graph = graph_builder.compile()