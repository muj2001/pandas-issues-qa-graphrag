# Milestone 1: Ingestion

## Concepts

- REST pagination: How does the Jira API paginate search results, and how will you know the fetch is complete?
- Rate limiting and retries: Which responses should trigger a retry, and how long should the script wait?
- Idempotent, resumable jobs: What state must survive an interrupted run? How will you detect duplicates or gaps?
- Raw and processed layers: Why save the original response before converting Jira markup to text?

## Learning Outcomes

- Explain how pagination, checkpoints, and retries work together in a resumable fetch.
- Separate immutable raw issue data from derived, re-runnable transformations.
- Convert fetched issues into readable text without losing their identifiers or resolution context.

## Tasks

- Write a fetch script with JQL, pagination, retries, and a checkpoint file.
- Save raw JSON to disk.
- Write a transform step that converts Jira markup to clean text and serializes each issue into a readable block (key, type, status, title, description, resolution).

## Acceptance Criteria

- The script can be stopped and restarted without duplicating or losing issues.
- Raw data and cleaned text are in separate folders.
- You can print any issue as clean text.

## Learning Check

Why save raw data before transforming? What would break if you didn't?
