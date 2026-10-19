# Milestone 7: LLM Extraction and GraphRAG

## Concepts

- Schema-guided versus open extraction: How does a fixed schema constrain what the LLM can add to the graph?
- Extraction noise: How will you spot incorrect or unsupported entities and relationships?
- Graph retrieval: How do seed issues, neighborhood expansion, and text-to-Cypher differ?
- Hybrid vector and graph retrieval: Which question types might justify the added graph work?

## Learning Outcomes

- Extract and spot-check schema-constrained entities and relations from issue text.
- Connect vector retrieval to graph expansion for multi-hop questions.
- Compare vector-only, graph-assisted, and hybrid results by question type and cost.

## Tasks

- Use an LLM to extract entities and relations from descriptions and comments, restricted to your schema. Spot-check a sample for accuracy.
- Implement graph-assisted retrieval: vector search finds seed issues, then expand through links or shared components, then pass the expanded set to the LLM.
- Optionally try text-to-Cypher for structured questions.
- Run the multi-hop and aggregation questions through three systems: vector-only, graph-assisted, and hybrid.

## Acceptance Criteria

- Extraction quality is measured on a hand-checked sample (precision at least roughly reported).
- A comparison table shows results across systems by question type.

## Learning Check

Where did the graph help, where did it add cost without benefit, and what would you do differently next time?
