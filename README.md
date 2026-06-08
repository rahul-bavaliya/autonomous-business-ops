# Autonomous Business Operations Agent Platform

An AI-powered multi-agent platform that combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), semantic search, and workflow orchestration to automate business operations.

The long-term vision is to create a team of AI agents that can perform research, retrieve company knowledge, make decisions, collaborate, and execute business workflows autonomously.

---

# Features

## Research Agent

- Internet research using DuckDuckGo Search
- AI-powered report generation using NVIDIA NIM
- Structured JSON outputs
- Search quality evaluation
- Conditional workflow routing using LangGraph

## Knowledge Agent (RAG)

- NVIDIA Embeddings (`nv-embed-v1`)
- ChromaDB Vector Database
- Semantic Search
- Document Ingestion Pipeline
- Retrieval-Augmented Generation (RAG)
- Company Knowledge Base Support

## Workflow Engine

- LangGraph
- Stateful Agent Workflows
- Conditional Routing
- Modular Node Architecture
- Extensible Multi-Agent Design

## Logging & Monitoring

- Structured Logging
- Execution Tracing
- Workflow Visibility
- Agent Activity Monitoring

---

# Current Architecture

```text
                          User
                            │
                            ▼
                     LangGraph Router
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼

        Research Agent          Knowledge Agent
        (Internet Search)       (RAG Search)

                │                       │
                ▼                       ▼

         DuckDuckGo Search       ChromaDB Vector Store
                │                       │
                ▼                       ▼

         NVIDIA Nemotron         NVIDIA Embeddings

                └───────────┬───────────┘
                            │
                            ▼
                         Response
```

---

# Tech Stack

## AI / LLM

- NVIDIA NIM
- NVIDIA Nemotron
- NVIDIA Embeddings

## Agent Framework

- LangGraph

## Vector Database

- ChromaDB

## Search

- DuckDuckGo Search

## Language

- Python 3.12+

## Validation

- Pydantic

## Logging

- Python Logging

---

# Project Structure

```text
autonomous-business-ops/

│
├── app/
│
├── config/
│   └── settings.py
│
├── embeddings/
│   ├── embedding_service.py
│   └── vector_store.py
│
├── ingestion/
│   ├── chunker.py
│   └── ingest_documents.py
│
├── models/
│   ├── report.py
│   └── state.py
│
├── rag/
│   └── retriever.py
│
├── services/
│   ├── llm_service.py
│   ├── rag_service.py
│   └── research_service.py
│
├── tools/
│   ├── file_tool.py
│   └── search_tool.py
│
├── utils/
│   └── logger.py
│
├── workflows/
│   └── research_graph.py
│
├── documents/
│
├── outputs/
│
├── vector_db/
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

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

Create a `.env` file in the root directory:

```env
NVIDIA_NIM_API_KEY=nvapi-****
NVIDIA_NIM_API_URL=https://integrate.api.nvidia.com/v1
CHAT_MODEL=nvidia/nemotron-3-super-120b-a12b
EMBEDDING_MODEL=nvidia/nv-embed-v1
```

---

# Running Research Agent

Start the application:

```bash
python -m app.main
```

Example:

```text
Research Topic:
LangGraph
```

Output:

```text
TITLE
LangGraph Overview

SUMMARY
LangGraph is a framework for building stateful AI agents...
```

Generated reports are stored in:

```text
outputs/
```

---

# Running Document Ingestion

Place text files inside:

```text
documents/
```

Example:

```text
documents/

    langgraph.txt
    mcp.txt
    ai_agents.txt
```

Run ingestion:

```bash
python -m app.ingestion.ingest_documents
```

Example output:

```text
Stored: langgraph_0
Stored: mcp_0
Stored: ai_agents_0
```

Embeddings are stored in:

```text
vector_db/
```

---

# Testing Retrieval

Run:

```bash
python -m app.test_retrieval
```

Example:

```text
What is LangGraph?
```

Output:

```text
LangGraph is a framework for building stateful AI agents.
```

---

# Testing RAG

Run:

```bash
python -m app.test_rag
```

Example:

```text
Question:
What is LangGraph?
```

Output:

```text
LangGraph is a framework for building stateful AI agents...
```

---

# Example Workflow

## Research Workflow

```text
User Query
      │
      ▼
Search Node
      │
      ▼
Search Evaluation Node
      │
      ▼
Research Node
      │
      ▼
Save Node
      │
      ▼
JSON Report
```

---

## RAG Workflow

```text
Question
      │
      ▼
Embedding
      │
      ▼
Vector Search
      │
      ▼
Relevant Chunks
      │
      ▼
NVIDIA Nemotron
      │
      ▼
Answer
```

---

# Development Roadmap

## Completed

### Milestone 1

- NVIDIA NIM Integration
- LLM Service

### Milestone 2

- Search Tool
- Research Service

### Milestone 3

- LangGraph Workflow
- Routing Logic

### Milestone 4

- Logging
- Search Evaluation

### Milestone 5

- NVIDIA Embeddings
- ChromaDB
- Retriever
- RAG Service

---

## Next Milestones

### Milestone 6

Hybrid Agent Router

```text
Question
    │
    ▼
Router
    │
 ┌──┴──┐
 │     │
 ▼     ▼

RAG   Search
```

### Milestone 7

Agent Memory

- Conversation History
- Persistent Memory
- Long-Term Knowledge

### Milestone 8

Multi-Agent System

- Research Agent
- Knowledge Agent
- Planner Agent
- Supervisor Agent

### Milestone 9

MCP Integration

- Tool Discovery
- External Systems
- Standardized Tool Access

### Milestone 10

Autonomous Business Operations Platform

- Sales Agent
- HR Agent
- Operations Agent
- Finance Agent
- Executive Agent

---

# Learning Goals

This project is designed to provide hands-on experience with:

- AI Agents
- LangGraph
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- NVIDIA NIM
- Embeddings
- Semantic Search
- Multi-Agent Systems
- MCP (Model Context Protocol)
- Autonomous AI Systems

---

# License

MIT License

---

# Author

Rahul Bavaliya

Software Developer | AI Engineer

Location: Regina, Saskatchewan, Canada

Focus Areas:

- Artificial Intelligence
- Machine Learning
- Agentic AI Systems
- Autonomous Business Operations