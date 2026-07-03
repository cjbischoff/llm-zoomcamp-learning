# Module 03 Homework — AI Orchestration with Kestra

Answers for the [Module 03 homework](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/03-orchestration/homework.md).

## Question 1: Context Engineering

**Answer:** AI Copilot has access to current Kestra plugin documentation

Kestra's AI Copilot references current plugin docs

## Question 2: RAG vs No RAG

**Answer:** Vague, generic, or fabricated — the model guesses from training data

Running `1_chat_without_rag.yaml` produces confident-sounding features (e.g. UI redesign, flow templates) that are not grounded in the actual Kestra 1.1 release notes. `2_chat_with_rag.yaml` ingests the real release documentation and gives accurate, specific answers.

## Question 3: Token usage — short summary

**Answer:** 60-100 tokens

Run `4_simple_agent.yaml` with `summary_length = short`. In the `log_token_usage` task logs, check **Multilingual Agent → Output tokens**.

Example result: ~84 output tokens.

## Question 4: Token usage — long summary

**Answer:** 2-5x more

Run `4_simple_agent.yaml` with `summary_length = long` and compare **Multilingual Agent → Output tokens** to Question 3.

Short = 1-2 sentences; long = 1-3 paragraphs, so expect roughly 2-5× more output tokens.

## Question 5: Modifying a flow

**Answer:** 2-4x more

In `4_simple_agent.yaml`, change the `english_brevity` prompt from exactly **1 sentence** to exactly **3 sentences**. Save, then run with `summary_length = long`.

Compare **English Brevity Agent → Output tokens** to the original 1-sentence version (also with `summary_length = long`). Three sentences vs one → roughly 2-4× more output tokens.

## Question 6: Best Practices

**Answer:** Use traditional task-based workflows for predictability and auditability

For production workflows that need deterministic, repeatable, auditable results (e.g. financial reporting, regulated industries), use traditional task-based workflows—not open-ended AI agents.
