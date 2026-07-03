# LLM Zoomcamp Learning

Homework, experiments, and notes for [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp).

## Setup

```bash
uv sync
# create .env with OPENAI_API_KEY=sk-...
# module 02: cd homework/module-02 && uv run python download.py
# module 03: cd homework/module-03 && ./setup-secrets.sh && docker compose up -d
```

## Structure

- `homework/module-01/` — Module 01 homework (RAG, chunking, agent)
- `homework/module-02/` — Module 02 homework (embeddings, vector search, hybrid RRF)
- `homework/module-03/` — Module 03 homework (Kestra, AI Copilot, RAG, agents)
- `experiments/` — Lesson practice notebooks and scripts
- `notes/` — Learning notes

## Stack

Python 3.13, `uv`, Jupyter, minsearch, gitsource, OpenAI, toyaikit, ONNX embedder, Kestra
