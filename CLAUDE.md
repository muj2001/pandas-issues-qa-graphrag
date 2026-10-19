# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state

This repository is a project plan, not an implemented application. Read `project-kafka-docs-qa-graphrag.md` for scope and the relevant page in `docs/milestones/` for milestone details before making architecture decisions. Despite the directory name, the planned corpus is public Apache Kafka **Jira issues**, not Kafka documentation. There is no README, application code, dependency manifest, build, lint, or test command yet; do not invent commands. Add verified setup and single-test commands here once they exist.

## Intended architecture

The plan describes an incremental Python, local-first Q&A system. First, fetch a bounded slice of Jira issues and comments through the public API, saving immutable raw JSON. Transform Jira markup into readable issue text; chunk, embed, and index it for vector retrieval. Later, add keyword retrieval, fusion, and reranking before passing retrieved context to an LLM for answers with ticket-key citations. Build the graph track only after the retrieval baseline: first from structured Jira fields, then from schema-guided LLM extraction. Compare vector-only, graph-assisted, and hybrid retrieval using a human-written eval set and recorded retrieval/answer results. See the project plan for milestone acceptance criteria and scope limits; these components are not implemented yet.

The starting choices in the plan are Python scripts, local storage, and DeepSeek via API for generation; embedding model, vector store, and graph database are not final decisions. Preserve the separation between raw data and derived artifacts so experiments can be rerun without fetching Jira again.

## Collaboration

The user knows Python but is learning AI engineering. When they request implementation, Claude Code can do most of the coding; keep them involved in architecture choices, explain how changed pieces connect, and leave room for their code review. The user wants to research concepts and topics themselves, so discuss what to investigate and why rather than doing that research for them unless asked. Work milestone by milestone and make evaluation results visible before recommending added complexity.
