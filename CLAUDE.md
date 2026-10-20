# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state

This repository is a project plan, not an implemented application. Read `project-pandas-issues-qa-graphrag.md` for scope and the relevant page in `docs/milestones/` for milestone details before making architecture decisions. Despite the directory name, the planned corpus is public `pandas-dev/pandas` GitHub issues, not Kafka documentation or Jira data. There is no README, application code, dependency manifest, build, lint, or test command yet; do not invent commands. Add verified setup and single-test commands here once they exist.

## Intended architecture

The plan describes an incremental Python, local-first Q&A system. First, fetch a bounded slice of GitHub issues and comments through the public API, saving immutable raw JSON. The repository `/issues` endpoint also returns PRs: exclude those from the issue-text corpus, but retain linked PR data for graph work. Transform GitHub Markdown into readable issue text; chunk, embed, and index it for vector retrieval. Later, add keyword retrieval, fusion, and reranking before passing retrieved context to an LLM for answers with issue-number and URL citations. Build the graph track only after the retrieval baseline: fetch and save raw timelines and linked PRs, then model structured GitHub relationships before schema-guided LLM extraction. Compare vector-only, graph-assisted, and hybrid retrieval using a human-written eval set and recorded retrieval/answer results. See the project plan for milestone acceptance criteria and scope limits; these components are not implemented yet.

The starting choices in the plan are Python scripts, local storage, and DeepSeek via API for generation; embedding model, vector store, and graph database are not final decisions. Preserve the separation between raw data and derived artifacts so experiments can be rerun without refetching GitHub records.

## Collaboration

The user knows Python but is learning AI engineering. When they request implementation, Claude Code can do most of the coding; keep them involved in architecture choices, explain how changed pieces connect, and leave room for their code review. The user wants to research concepts and topics themselves, so discuss what to investigate and why rather than doing that research for them unless asked. Work milestone by milestone and make evaluation results visible before recommending added complexity.
