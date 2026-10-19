# Milestone 6: Graph Schema and Structured Graph

## Concepts

- Nodes, edges, and properties: Which Jira facts are entities, relationships, or attributes?
- Schema design from questions: Which relationship types are needed to answer your actual multi-hop questions?
- Entity resolution: How will you recognize when two records refer to the same person?
- Graph queries: What can a direct Cypher or NetworkX query answer without an LLM?

## Learning Outcomes

- Derive a small graph schema from questions instead of modeling every available field.
- Build and query a graph using structured Jira fields.
- Identify questions a structured graph helps answer and those it does not.

## Tasks

- Write down 10 to 20 questions the graph should answer. Derive the schema from them (entity types, relationship types, properties). Keep it small.
- Build the graph from structured Jira fields only: issue links, parent/epic, component, fix version, assignee/reporter.
- Write a few Cypher (or NetworkX) queries that answer your multi-hop eval questions directly.

## Acceptance Criteria

- The schema is documented in the repo, with the questions that justify each type.
- At least 5 multi-hop questions are answered correctly through graph queries alone.
- People are deduplicated into single nodes.

## Learning Check

Which questions did the schema make easy, and which did it not help with?
