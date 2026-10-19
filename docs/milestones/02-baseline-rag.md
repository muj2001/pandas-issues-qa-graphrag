# Milestone 2: Baseline RAG

## Concepts

- Embeddings and similarity search: What information can an embedding capture, and what does it miss?
- Chunking: What makes an issue too long to embed as one unit? What context must each chunk retain?
- Top-k retrieval: How does the number of retrieved chunks affect answer quality and context size?
- Metadata filtering: Which questions need structured filters before or after vector search?

## Learning Outcomes

- Build a question-to-answer path from issue chunks through retrieval to a cited response.
- Explain what the embedding model sees and identify a retrieval failure from your own results.
- Reindex an individual issue without rebuilding the whole index.

## Tasks

- Chunk per issue (split only long ones), with the key and title repeated in every chunk.
- Embed and index chunks with metadata (key, status, component, dates, URL).
- Build a CLI: question in, top-k chunks out, LLM answer with ticket keys cited.

## Acceptance Criteria

- Answers cite real ticket keys from retrieved chunks.
- Metadata filters work (for example, only resolved bugs in a component).
- Chunk IDs follow a scheme that lets you delete and reindex one ticket (for example `KAFKA-123#comments-2`).

## Learning Check

What does the embedding model see, and what can't it capture? Give one failure you observed.
