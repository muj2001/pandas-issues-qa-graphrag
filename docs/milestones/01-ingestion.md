# Milestone 1: Ingestion

## Concepts

- REST pagination: How do GitHub issue and comment endpoints paginate, and how will you know the fetch is complete?
- Issue/PR distinction: Why does the `/issues` endpoint include PRs, and how does that affect the requested issue count?
- Rate limiting and retries: Which responses should trigger a retry, and how long should the script wait?
- Idempotent, resumable jobs: What state must survive an interrupted run? How will you detect duplicates or gaps?
- Raw and processed layers: Why save the original response before converting GitHub Markdown to text?

## Learning Outcomes

- Explain how pagination, checkpoints, and retries work together in a resumable fetch.
- Separate immutable raw issue data from derived, re-runnable transformations.
- Convert fetched issues into readable text without losing issue numbers, URLs, or closure context.

## Tasks

- Pick a fixed issue creation-date window. Paginate closed issues with `sort=created`; skip PR records identified by `pull_request`. Do not use `since` as a creation-date filter: it filters by update time.
- Fetch all pages of comments for each selected issue. Use retries, rate-limit handling, and a checkpoint to resume without fetching saved records again.
- Save raw issue and comment JSON to disk before transforming it.
- Convert GitHub Markdown into readable text and serialize each issue with its number, URL, title, body, state, labels, dates, and comments.

## Acceptance Criteria

- The script can be stopped and restarted without duplicating or skipping issues or comments in the chosen slice.
- PRs do not enter the issue-text corpus; the number of issues is counted after filtering mixed API pages.
- Raw data and cleaned text are in separate folders.
- You can print any saved issue and its comments as clean text.

## Learning Check

Why save raw data before transforming? What would break if you didn't?
