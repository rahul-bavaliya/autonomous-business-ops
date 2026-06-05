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

    search_score: int

    retry_count: int

    report: dict


# ==================================================
# Router
# ==================================================

def router_node(
    state: ResearchState
):

    logger.info(
        "Running Router Node"
    )

    return {
        "route": "research"
    }


def route_query(
    state: ResearchState
):

    return state["route"]


# ==================================================
# Search
# ==================================================

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


# ==================================================
# Search Evaluation
# ==================================================

def evaluate_search_node(
    state: ResearchState
):

    logger.info(
        "Running Search Evaluation Node"
    )

    result_count = state.get(
        "search_result_count",
        0
    )

    score = 0

    if result_count >= 5:
        score = 10

    elif result_count >= 3:
        score = 7

    elif result_count >= 1:
        score = 4

    logger.info(
        f"Search score: {score}"
    )

    return {
        "search_score": score
    }


def route_after_evaluation(
    state: ResearchState
):

    score = state.get(
        "search_score",
        0
    )

    logger.info(
        f"Routing using score: {score}"
    )

    if score >= 7:

        logger.info(
            "Routing to Research Node"
        )

        return "research"

    logger.warning(
        "Routing to Retry Search Node"
    )

    return "retry"


# ==================================================
# Retry Search
# ==================================================

def retry_search_node(
    state: ResearchState
):

    logger.info(
        "Running Retry Search Node"
    )

    retry_count = state.get(
        "retry_count",
        0
    )

    retry_count += 1

    logger.info(
        f"Retry count: {retry_count}"
    )

    if retry_count >= 2:

        logger.warning(
            "Maximum retries reached"
        )

        return {
            "retry_count": retry_count,
            "route": "end"
        }

    return {
        "retry_count": retry_count
    }


def route_after_retry(
    state: ResearchState
):

    retry_count = state.get(
        "retry_count",
        0
    )

    if retry_count >= 2:
        return "end"

    return "search"


# ==================================================
# Research
# ==================================================

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


# ==================================================
# Save
# ==================================================

def save_node(
    state: ResearchState
):

    logger.info(
        "Running Save Node"
    )

    filename = (
        "output_" +
        datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )
    )

    file_tool.save_json(
        filename=filename,
        data=state["report"]
    )

    return {}


# ==================================================
# Graph
# ==================================================

graph_builder = StateGraph(
    ResearchState
)

graph_builder.add_node(
    "router",
    router_node
)

graph_builder.add_node(
    "search",
    search_node
)

graph_builder.add_node(
    "evaluate_search",
    evaluate_search_node
)

graph_builder.add_node(
    "retry_search",
    retry_search_node
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
        "research": "search"
    }
)

graph_builder.add_edge(
    "search",
    "evaluate_search"
)

graph_builder.add_conditional_edges(
    "evaluate_search",
    route_after_evaluation,
    {
        "research": "research",
        "retry": "retry_search"
    }
)

graph_builder.add_conditional_edges(
    "retry_search",
    route_after_retry,
    {
        "search": "search",
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