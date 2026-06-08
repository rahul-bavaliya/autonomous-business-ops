# Autonomous Business Operations Agent Platform

An AI-powered multi-agent platform that combines:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Internet Research
- Agent Memory
- Query Rewriting
- Multi-Agent Routing
- Workflow Orchestration

The long-term goal is to build an autonomous team of AI agents capable of researching, retrieving knowledge, planning, collaborating, and executing business workflows.

---

# Features

## Knowledge Agent (RAG)

- NVIDIA Embeddings (`nv-embed-v1`)
- ChromaDB Vector Database
- Semantic Search
- Hybrid Retrieval
- Keyword Search
- Reranking
- Query Rewriting
- Conversational RAG
- Memory-Aware Retrieval

---

## Research Agent

- DuckDuckGo Search
- Web Research
- Structured Research Reports
- JSON Output Validation
- Search Result Summarization
- External Knowledge Retrieval

---

## Router Agent

Routes questions to the appropriate agent.

### Knowledge Route

Used when the question is likely answerable from the internal knowledge base.

Example:

```text
What is LangGraph?
Who created it?
```

### Research Route

Used when the question requires external information.

Example:

```text
What is Saskatchewan?
Latest NVIDIA stock news
Current weather in Regina
```

---

## Intelligent Fallback

If the Knowledge Agent cannot answer from the knowledge base:

```text
Knowledge Agent
        ↓
"No answer found"
        ↓
Research Agent
        ↓
Final Response
```

This prevents failed responses and allows the system to answer questions outside the local knowledge base.

---

## Memory

Conversation memory enables:

- Follow-up questions
- Context awareness
- Query rewriting
- Multi-turn conversations

Example:

```text
User:
What is LangGraph?

User:
Who created it?
```

Query Rewriter converts:

```text
Who created it?
```

into:

```text
Who created LangGraph?
```

before retrieval.

---

## Logging & Monitoring

- Structured Logging
- Agent Selection Logs
- Retrieval Logs
- Search Logs
- RAG Tracing
- Memory Visibility

---

# Current Architecture

```text
                               User
                                 │
                                 ▼

                         Router Agent
                                 │
                 ┌───────────────┴───────────────┐
                 │                               │
                 ▼                               ▼

          Knowledge Agent                Research Agent
             (RAG)                       (Internet)

                 │                               │
                 ▼                               ▼

          Query Rewriter                 DuckDuckGo Search
                 │
                 ▼

        Hybrid Retriever
       ┌────────┴────────┐
       │                 │
       ▼                 ▼

 Vector Search     Keyword Search
       │                 │
       └────────┬────────┘
                ▼

           Reranker
                │
                ▼

        NVIDIA Nemotron
                │
                ▼

            Response

```

---

# Project Structure

```text
app/

├── agents/
│   ├── knowledge_agent.py
│   ├── query_rewriter.py
│   ├── research_agent.py
│   └── router_agent.py
│
├── config/
│   └── settings.py
│
├── documents/
│   └── langgraph.txt
│
├── embeddings/
│   ├── embedding_service.py
│   └── vector_store.py
│
├── ingestion/
│   ├── chunker.py
│   └── ingest_documents.py
│
├── llm/
│   ├── llm_service.py
│   └── nvidia_client.py
│
├── memory/
│   ├── conversation_memory.py
│   └── memory_manager.py
│
├── prompts/
│   └── system_prompts.py
│
├── rag/
│   ├── retriever.py
│   ├── keyword_retriever.py
│   ├── hybrid_retriever.py
│   └── reranker.py
│
├── schemas/
│   ├── base.py
│   └── research.py
│
├── services/
│   ├── rag_service.py
│   └── research_service.py
│
├── tools/
│   ├── search_tool.py
│   ├── file_tool.py
│   └── date_tool.py
│
├── utils/
│   ├── logger.py
│   └── json_parser.py
│
├── workflows/
│   └── research_graph.py
│
├── main.py
├── main_router.py
└── tests
```

---

# Tech Stack

## LLM

- NVIDIA Nemotron 120B
- NVIDIA NIM

## Embeddings

- NVIDIA NV-Embed-v1

## Vector Database

- ChromaDB

## Agent Framework

- LangGraph

## Search

- DuckDuckGo Search

## Validation

- Pydantic

## Language

- Python 3.12+

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/autonomous-business-ops.git

cd autonomous-business-ops
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
NVIDIA_NIM_API_KEY=YOUR_API_KEY
NVIDIA_NIM_API_URL=https://integrate.api.nvidia.com/v1
CHAT_MODEL=nvidia/nemotron-3-super-120b-a12b
EMBEDDING_MODEL=nvidia/nv-embed-v1
```

---

# Document Ingestion

Add documents:

```text
documents/

    langgraph.txt
    ai_agents.txt
    company_wiki.txt
```

Run:

```bash
python -m app.ingestion.ingest_documents
```

Output:

```text
Stored:
langgraph_0
langgraph_1
langgraph_2
```

---

# Run Multi-Agent Router

Start:

```bash
python -m app.main_router
```

Example:

```text
Question:
What is LangGraph?
```

Output:

```text
KNOWLEDGE AGENT

LangGraph is a framework for building stateful AI agents.
```

---

Example:

```text
Question:
What is Saskatchewan?
```

Output:

```text
RESEARCH AGENT

Saskatchewan is a province in Western Canada...
```

---

# Example Conversation

```text
User:
What is LangGraph?

Assistant:
LangGraph is a framework for building stateful AI agents.

User:
Who created it?

Query Rewriter:
Who created LangGraph?

Assistant:
LangGraph was created by LangChain.
```

---

# Retrieval Pipeline

```text
User Question
       │
       ▼

Query Rewriter
       │
       ▼

Hybrid Retrieval
       │
 ┌─────┴─────┐
 │           │

Vector     Keyword
Search     Search

 │           │
 └─────┬─────┘
       ▼

Reranker
       ▼

Top Chunks
       ▼

LLM Answer
```

---

# Current Progress

## Completed

### Phase 1

- NVIDIA NIM Integration
- LLM Service

### Phase 2

- Search Tool
- Research Service

### Phase 3

- LangGraph Workflow

### Phase 4

- ChromaDB Integration
- Embedding Service
- Vector Search

### Phase 5

- Knowledge Agent
- RAG Pipeline
- Query Rewriting
- Memory

### Phase 6

- Hybrid Retrieval
- Keyword Search
- Reranking

### Phase 7

- Router Agent
- Knowledge ↔ Research Routing
- Research Fallback

---

# Next Roadmap

## Planner Agent

Break large goals into tasks.

```text
Goal
  ↓
Planner
  ↓
Tasks
```

---

## Supervisor Agent

Manage multiple agents.

```text
Supervisor
    │
 ┌──┼──┐
 │  │  │

Research
Knowledge
Execution
```

---

## MCP Integration

- Tool Discovery
- External Systems
- Standardized Tool Usage

---

## Autonomous Business Operations

Future specialized agents:

- Sales Agent
- HR Agent
- Finance Agent
- Operations Agent
- Executive Agent

---

# Learning Goals

This project demonstrates:

- Agentic AI
- RAG Systems
- ChromaDB
- NVIDIA NIM
- LangGraph
- Multi-Agent Systems
- Query Rewriting
- Memory Systems
- Hybrid Search
- Autonomous AI Architectures

---

# License

MIT License

---

# Author

**Rahul Bavaliya**

Software Developer | AI Engineer

Regina, Saskatchewan, Canada

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Agentic AI
- Multi-Agent Systems
- Autonomous Business Operations