# llm-zoomcamp-learning

**Purpose:** Public learning repo for LLM Zoomcamp 2026 cohort.
Homework, notebooks, and notes. Homework submissions must be public for grading.
The capstone lives in a separate repo: `llm-zoomcamp-security-assistant`.

## Folder Map

One folder per course module at the repo root, matching the official module names:

```
llm-zoomcamp-learning/
├── 01-agentic-rag/
│   ├── homework/     ← homework answers and submission files
│   └── lessons/      ← exploration notebooks and code
├── 02-vector-search/
│   ├── homework/
│   └── lessons/
├── 03-orchestration/
│   ├── homework/
│   └── lessons/
├── (add folders as modules publish)
├── .gitignore        ← must include __pycache__/, .env, *.pyc
├── pyproject.toml
├── uv.lock
└── README.md
```

Use `uv` for Python package management (`uv add <package>`, not `pip install`).

## Homework Submissions

Homework requires a **public GitHub repo link** for submission. This repo serves that purpose.
Each module's homework lives in `<module-name>/homework/` with its own README covering answers and setup.

**Important:** Keep `__pycache__/` out of git — add it to `.gitignore` from day one.

## Homework Status (as of 2026-06-15)

| Module | Status |
|--------|--------|
| Module 01 | ✅ Published — check `cohorts/2026/` for questions |
| Module 02 | Not yet published |
| Module 03 | ✅ Published — 6 Kestra questions, 6-8 hrs |
| Module 04 | Not yet published |
| Module 05 | Not yet published |
| Module 06 | Not yet published (optional) |
| Module 07 | Not yet published (optional) |
| Workshop (dlt) | Optional — sign-up based |

Check `cohorts/2026/` in the official GitHub repo for updates.

## What This Repo Is NOT

- Not the capstone submission repo
- Not production code
- Not mixed with `app/` code from the capstone

## Scope

Help with:
- Debugging homework problems and notebook code
- Explaining course concepts
- Working through module exercises

Course context lives in the sibling research repo (`topic_zoomcamp-llm`):
- Synthesis documents: `synthesis/module-XX-*.md`
- Master index: `synthesis/zoomcamp-llm.md`
- Capstone plan: `synthesis/capstone-project-plan.md`

## Git

Commit after each module session:
- `homework: complete module-XX questions`
- `lessons: module-XX exploration notebooks`
- `notes: module-XX video notes`
