# Milestone 3: Eval Set and Baseline Numbers

## Concepts

- Recall@k and MRR: What does each metric reward, and how do they behave when a question has multiple relevant issues?
- Human-written test questions: What would make a generated question set misleadingly easy?
- Train/test leakage: How can changing the system after seeing eval answers bias later comparisons?
- Question types: Why report exact-term, symptom-style, similar-issue, and multi-hop results separately?

## Learning Outcomes

- Build a versioned eval set with known relevant GitHub issue numbers and question-type labels.
- Reproduce baseline retrieval numbers and diagnose failures by question type.
- Distinguish a measured result from a hypothesis about its cause.

## Tasks

- Write 50 to 100 real questions by hand, each with the relevant issue number(s) from the ingested slice. Include a mix: exact-term, symptom-style, similar-issue, and multi-hop questions (tag them).
- Write a script that runs retrieval on all questions and reports recall@k and MRR, broken down by question type.
- Record baseline numbers in a results log.

## Acceptance Criteria

- The eval file is human-written, versioned, and separate from anything used to build the system.
- One command reproduces the numbers.

## Learning Check

Which question types fail most, and what do you think causes it? Write the hypothesis before fixing anything.
