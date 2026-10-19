# Milestone 4: Better Retrieval

## Concepts

- Chunking variants and parent-child retrieval: How can you search small passages while preserving enough issue context to answer?
- Hybrid search: When should keyword matches complement dense similarity?
- Rank fusion: How can results from different retrieval methods be combined?
- Cross-encoder reranking: What does a reranker examine that a vector search does not?

## Learning Outcomes

- Compare chunking strategies using the same eval set.
- Explain the separate contribution of keyword retrieval, fusion, and reranking.
- Interpret per-question-type changes in recall@k and MRR, including changes that do not help.

## Tasks

- Compare at least two chunking strategies (for example, per-issue vs. description/comment-window split).
- Add keyword search and fuse with dense results.
- Add a reranker over the top 20 to 50 candidates.
- Re-run evals after each change.

## Acceptance Criteria

- A results table shows each change's effect on recall@k and MRR, per question type.
- You can state which change helped most and which didn't help.

## Learning Check

Which improvement surprised you? Why do exact terms like ticket keys and error codes need keyword search?
