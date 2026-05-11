# AGENTS.MD

Persistent context for coding agents working in this repository.

## Project Purpose

This repository is a personal learning project for building a lightweight IT support chatbot/agent. The project is intended to help the owner learn modern enterprise-style Python AI application patterns, especially:

- Python backend development
- LangChain document retrieval and RAG
- LangGraph workflow orchestration
- Clean project organization
- Support-ticket summarization and escalation workflows
- PyCharm / JetBrains development workflow
- Optional TypeScript frontend work later

The project should remain beginner-friendly, but organized professionally enough to discuss in an internship context.

## Important Data-Safety Rule

Do not use real company, customer, employee, ticket, credential, internal documentation, onboarding, or proprietary data.

This project must use only fake, synthetic, sample documentation and tickets. Do not add anything that appears to come from PNC or any real employer/client/internal system. Do not imply this project is affiliated with PNC.

Recommended README disclaimer:

```text
This is a personal learning project using entirely synthetic documentation and fake support tickets. It is not affiliated with PNC and does not use any proprietary, internal, customer, employee, or confidential data.
```

## Product Concept

The app should act like an internal-style IT support assistant. Example questions:

- "How do I reset a user's access?"
- "What are the steps to troubleshoot a login issue?"
- "Summarize this support ticket and suggest the next action."
- "Should this issue be escalated? If so, to which team?"

Core behavior:

1. Load fake support documentation.
2. Retrieve relevant document chunks.
3. Generate grounded answers using an LLM.
4. Cite fake source documents.
5. Route complex requests through a LangGraph workflow.
6. Summarize fake support tickets and recommend escalation teams.

## Recommended MVP

Start with a command-line app before adding any frontend.

Current direction:

- Keep Phase 1 intentionally thin: a runnable CLI baseline plus simple intent detection.
- Do not spend much time building a full rule-based chatbot.
- Move quickly into the main learning goal: LangChain, local RAG, and then LangGraph.
- Use free/local models through Ollama where possible.

MVP scope:

- Python CLI chat interface
- Fake markdown docs under `docs/`
- Document loading and chunking
- Local vector store for retrieval
- LangChain RAG chain
- Simple LangGraph workflow
- Source citations
- Fake ticket summarization
- Basic escalation recommendation

Avoid in the MVP:

- Authentication
- Real company integrations
- Real ticketing-system integrations
- Production deployment
- Complex multi-agent behavior
- Frontend UI

## Suggested Architecture

Near-term architecture path:

```text
Phase 1
User CLI
  -> IntentClassifier
  -> detected intent

Phase 2
User CLI
  -> fake docs in docs/
  -> LangChain document loader
  -> text splitter
  -> Ollama embeddings
  -> Chroma vector store
  -> retriever
  -> Ollama chat model
  -> grounded answer with sources

Phase 3
User CLI
  -> LangGraph workflow
      -> classify intent
      -> retrieve docs
      -> answer question
      -> summarize ticket when relevant
      -> recommend escalation when relevant
```

Longer-term architecture:

```text
User CLI
  -> LangGraph support workflow
      -> classify intent
      -> retrieve fake docs
      -> answer question with RAG
      -> summarize ticket when relevant
      -> recommend escalation when relevant
  -> final response with sources and next action
```

## Suggested Folder Structure

```text
it-support-agent/
├── README.md
├── AGENTS.MD
├── pyproject.toml
├── .env.example
├── docs/
│   ├── password_reset.md
│   ├── login_troubleshooting.md
│   ├── access_requests.md
│   ├── vpn_support.md
│   └── escalation_policy.md
├── src/
│   └── it_support_agent/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── document_loader.py
│       ├── vector_store.py
│       ├── prompts.py
│       ├── chains.py
│       ├── graph.py
│       ├── schemas.py
│       └── tools.py
├── tests/
│   ├── test_document_loader.py
│   ├── test_routing.py
│   └── test_ticket_summary.py
└── examples/
    ├── sample_questions.md
    └── sample_tickets.md
```

## Implementation Preferences

- Prefer small, clear modules over a single large script.
- Prefer deterministic routing rules where they are enough, and use LLM calls where they add clear value.
- Prioritize LangChain/RAG learning over expanding the Phase 1 rule-based implementation.
- Phase 1 should only prove the CLI/package structure and basic routing concept.
- Use Ollama for local/free model experimentation.
- Default chat model: `llama3.2`.
- Default embedding model: `nomic-embed-text`.
- Use Chroma as the initial local vector store.
- Keep prompts in `prompts.py` or a dedicated prompt module.
- Use Pydantic models for structured outputs once ticket summaries and escalation recommendations are added.
- Add focused tests for document loading, routing, and non-LLM business logic.
- Keep secrets out of the repository. Use `.env` locally and commit only `.env.example`.
- Do not overbuild early. The first usable version should be a CLI RAG app.

## Learning Roadmap

Phase 1: CLI baseline

- Build a runnable Python package with a CLI loop and simple intent classifier.
- Learn Python project layout, imports, editable installs, CLI input/output, and basic routing.
- Stop after the CLI can classify and print intent. Do not build a large rule-based assistant.

Phase 2: LangChain local RAG setup

- Add `pyproject.toml`, `.env.example`, and `config.py`.
- Use `python-dotenv` to load model names and docs path.
- Use Ollama locally for chat and embeddings.
- Add markdown docs, LangChain loaders, chunking, metadata, Chroma, and retrieval.
- Learn document preparation, embeddings, vector stores, semantic search, and local model configuration.

Phase 3: First RAG answer flow

- Connect retriever, prompt, LLM, and response formatting.
- Learn RAG, prompt templates, grounding, and citations.

Phase 4: LangGraph workflow

- Add nodes for intent classification, retrieval, answering, summarization, and escalation.
- Learn graph state, nodes, edges, and conditional routing.

Phase 5: Structured outputs

- Use Pydantic models for summaries and escalation recommendations.
- Learn validation and backend-friendly response shapes.

Phase 6: Tests and evaluation

- Add unit tests and sample question cases.
- Learn regression testing for AI-assisted workflows.

Phase 7: Optional API backend

- Add FastAPI endpoints after the CLI works.
- Learn request/response schemas and Python service organization.

Phase 8: Optional TypeScript frontend

- Add React/TypeScript UI after the backend is stable.
- Learn frontend/backend integration.

## Environment Notes

Current setup notes:

- The project uses a `src/` layout with package code under `src/it_support_agent/`.
- `pyproject.toml` is being used instead of `requirements.txt`.
- The project has been installed in editable mode with `pip install -e .`.
- After editable install, run the CLI with:

```zsh
python -m it_support_agent.main
```

- Local model settings belong in `src/it_support_agent/config.py`.
- `.env.example` should contain safe sample values only:

```text
OLLAMA_CHAT_MODEL=llama3.2
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
DOCS_DIR=docs
```

Earlier setup issue:

```zsh
source .venv/bin/activate
```

It failed because `.venv/bin/activate` did not exist. If implementation begins, first inspect the repo and decide whether to create a virtual environment, likely with:

```zsh
python3 -m venv .venv
source .venv/bin/activate
```

Do not install dependencies or create large generated artifacts without a clear need.

## How To Explain This Project

A concise internship-style description:

```text
I built a small IT support agent using Python, LangChain, and LangGraph. It uses synthetic internal-style documentation for retrieval-augmented generation, classifies support requests, summarizes sample tickets, and recommends escalation paths. I structured it as a clean Python backend so I could understand how AI workflows, document retrieval, and enterprise-style support processes fit together.
```
