# IT Support Agent

A personal learning project for building a lightweight IT support chatbot using Python, LangChain, and LangGraph.

This project uses only synthetic documentation and fake support tickets. It is not affiliated with PNC and does not use any proprietary, internal, customer, employee, or confidential data.

## Current Status

Phase 1 created a thin CLI baseline with simple intent detection.

The project is now moving into Phase 2: LangChain local RAG setup.

## Learning Goals

- Understand how LangChain connects an LLM to documents and retrieval tools.
- Learn how embeddings and vector stores support retrieval-augmented generation.
- Use Ollama for local/free model experimentation.
- Keep the project organized as a clean Python package.
- Later, use LangGraph to model multi-step support workflows.

## Tech Stack

- Python
- LangChain
- Ollama
- Chroma
- python-dotenv
- LangGraph later

Default local models:

```text
Chat model: llama3.2
Embedding model: nomic-embed-text
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e .
```

Copy the sample environment file if you want local overrides:

```bash
cp .env.example .env
```

Install Ollama separately, then pull the local models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Run

After `pip install -e .`, run:

```bash
python -m it_support_agent.main
```

## Environment Variables

Safe sample values are stored in `.env.example`:

```text
OLLAMA_CHAT_MODEL=llama3.2
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
DOCS_DIR=docs
```

Do not commit a real `.env` file.

## Project Path

Near-term path:

```text
Phase 1: CLI baseline and simple intent detection
Phase 2: LangChain local RAG with synthetic markdown docs
Phase 3: First grounded answer flow with citations
Phase 4: LangGraph support workflow
```

## Data Safety

Use only fake documentation and synthetic tickets.

Do not use:

- Real company documentation
- Customer data
- Employee data
- Internal tickets
- Credentials
- Screenshots from internal systems
- Proprietary workflows

The `docs/` directory should simulate an internal IT knowledge base using fictional examples only.
