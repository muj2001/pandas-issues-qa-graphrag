# Project 1: pandas Issue Q&A, from RAG to GraphRAG

## 1. Purpose

Build a question-answering system over public `pandas-dev/pandas` GitHub issues. Start with plain vector RAG, improve it step by step with measurement, then add a knowledge graph layer for questions that need multi-hop reasoning.

**Why this project:** the corpus has bug reports, reproductions, comment threads, labels, and links to pull requests (PRs). PRs can supply fix and milestone context, but a reference alone is not proof that a PR fixed an issue. This makes the corpus useful for chunking, hybrid search, reranking, schema-guided graph extraction, and evaluation.

**Primary concepts:** RAG and search, prompt engineering, knowledge graphs, evals (foundation for Project 3).

**Example questions the finished system should handle (adapt issue numbers to the chosen slice)**
- "What reproduction demonstrates issue #48757's float16 bug?" (single-hop, RAG)
- "Find issues similar to this pandas traceback." (semantic and keyword search)
- "Which issues closed by merged PRs in milestone X share a label with issue #48757?" (multi-hop, graph)
- "What are the main themes among closed issues labeled `Regression`?" (broad, aggregation)

---

## 2. Learning Outcomes

By the end you should be able to:

1. Explain and implement an ingestion pipeline (fetch, store raw, transform, chunk, embed, index) and make it resumable.
2. Compare chunking strategies and justify a choice with measured retrieval results.
3. Implement hybrid retrieval (dense plus keyword) and a reranker, and explain what each adds.
4. Write prompts that produce grounded answers with GitHub issue citations and refuse when the context lacks the answer.
5. Design a small graph schema from a list of real questions, populate it from GitHub relationships, and extend it with LLM extraction.
6. Explain when vector-only, graph-assisted, or hybrid retrieval wins, backed by your own eval numbers.
7. Build and use a small human-written eval set (recall@k, MRR, answer quality checks).

---

## 3. Scope

**In scope**
- A bounded slice of closed `pandas-dev/pandas` issues from a fixed creation-date range, fetched via GitHub's public REST API; start small before scaling toward a few thousand
- Local-first stack: laptop, files, a local vector store
- CLI or minimal web UI for asking questions
- Graph layer built from GitHub labels, issue/PR links, PR milestones, and LLM extraction

**Out of scope**
- Scraping all of GitHub or multiple repositories
- Production deployment, auth, multi-user support
- Fine-tuning (that's Project 3)
- Fancy front end

---

## 4. Data

| Item | Decision |
|---|---|
| Source | Public `pandas-dev/pandas` GitHub REST API. Check current API docs and rate limits before building. |
| Starting slice | Closed issues created within a fixed date range; start with a small sample, then scale toward a few thousand |
| Issue fields | number, html_url, title, body, state, state_reason, labels, milestone, assignees, created_at, updated_at, closed_at, comments |
| Raw storage | JSON files on disk (one per issue or per page, plus separate comment/timeline/PR responses), never modified after saving |
| Comments | Fetch all pages of the per-issue comments endpoint; do not assume the issue list embeds comment bodies |
| Relationships | Fetch issue timeline events and linked PR details as raw JSON before graph construction in Milestone 6 |

GitHub's repository `/issues` endpoint mixes issues and PRs. Save the raw page, then use the `pull_request` field to exclude PRs from the issue-text corpus; fetch linked PRs separately for graph facts. A page of 100 records may contain fewer than 100 issues. Paginate until the chosen issue slice is complete, deduplicating by issue number. The `since` parameter filters by **updated** time, not creation time; use `sort=created` and an explicit creation-date window if selecting by creation date. Closed status is observed at fetch time; keep the raw snapshot for reproducibility.

Public API reads can be unauthenticated (60 requests/hour per IP); authenticated user requests normally allow 5,000/hour, subject to GitHub's other limits. Check the current limits, handle rate-limit responses and pagination, and avoid spending requests on already saved records.

**Rule:** always save raw JSON first. Each downstream transform must be re-runnable from saved raw issue, comment, timeline, and PR responses without refetching those records.

---

## 5. Architecture

```
GitHub API --> raw issue/comment JSON --> transform (Markdown -> text) --> chunker
                                                              |
                                  +---------------------------+
                                  v                           v
                           embeddings + vector store     keyword index (BM25)
                                  \                           /
                                   +-------- retriever ------+
                                                 |
                                             reranker
                                                 |
                                   context builder + prompt
                                                 |
                                               LLM
                                                 |
                                    answer + citations (issue # + URL)

Graph track (Milestones 6-7):
raw issue/timeline/PR JSON --> structured edges (labels, PR links, milestones)
                           --> LLM extraction (schema-guided) --> graph DB --> graph retriever
```

---

## 6. Suggested Stack (change if you have reasons)

| Layer | Starting choice | Notes |
|---|---|---|
| Language | Python | Plain scripts first; frameworks later, if at all |
| Fetching | `requests` plus checkpoint file | Paginate issue, comment, and timeline endpoints; respect primary and secondary rate limits |
| Embeddings | Small open model (for example a BGE or E5 variant) or a hosted embedding API | Decide in Milestone 2 and record why; switching later means re-embedding |
| Vector store | Chroma or Qdrant (local) | pgvector is an option if you want Postgres practice |
| Keyword search | `rank_bm25` or the store's built-in full-text | |
| Reranker | Open cross-encoder model | Added in Milestone 4 |
| LLM | DeepSeek via API (cost-friendly) | Keep it behind one small function so you can swap models |
| Graph | NetworkX for a first pass, then Neo4j (Docker) with Cypher | |
| Eval | Plain Python plus a JSON eval file | No eval framework until you know what you need |

---

## 7. Milestones (grouped by concept)

Each linked page contains research prompts, learning outcomes, tasks, acceptance criteria, and a learning check. The pages are the source of truth for milestone details.

1. [Ingestion](docs/milestones/01-ingestion.md): Fetch and preserve GitHub issues and comments, then transform them into readable text.
2. [Baseline RAG](docs/milestones/02-baseline-rag.md): Build chunked vector retrieval and cited answers.
3. [Eval set and baseline numbers](docs/milestones/03-eval-baseline.md): Write human-checked questions and measure retrieval performance.
4. [Better retrieval](docs/milestones/04-better-retrieval.md): Compare chunking, keyword search, fusion, and reranking.
5. [Grounded answers](docs/milestones/05-grounded-answers.md): Test citations and refusal behavior across prompt versions.
6. [Structured graph](docs/milestones/06-structured-graph.md): Design a schema from questions and query GitHub's structured relationships.
7. [LLM extraction and GraphRAG](docs/milestones/07-graphrag.md): Add extracted relationships and compare graph-assisted retrieval against the baseline.

---

## 8. Deliverables

- Repo with README (setup, how to run each milestone)
- `docs/decisions.md`: short log of each design choice and why (chunking, embedding model, schema)
- `eval/questions.json` and a results log with numbers per milestone
- Final write-up (1 to 2 pages): what worked, what didn't, vector vs. graph comparison

## 9. Definition of Done

- Pipeline runs end to end from raw JSON.
- Eval results exist for baseline, improved retrieval, and graph-assisted retrieval.
- You can explain every component without looking at the code.

## 10. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Fetching is slow or rate limited | Small slice first, checkpointing, authentication, polite delays |
| Eval set too easy or leaks into design | Write it by hand early; don't tune on every question |
| Graph extraction is noisy | Schema-guided extraction, spot-check, start from structured fields |
| Scope creep (more projects, fancy UI) | Stay within the scope in section 3 |
| Cost creep from LLM calls | Cache LLM outputs to disk, use a cheap model, extract on a subset first |

## 11. Handoff to Project 3

The eval set, raw data, and chunks from this project are the inputs for the eval harness and fine-tuning work in Project 3. Keep them clean and versioned.
