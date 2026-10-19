# Milestone 5: Prompt Engineering for Grounded Answers

## Concepts

- Grounding and citation formats: How can a reader verify a claim against a retrieved ticket?
- Missing or conflicting context: When should the system say it cannot answer?
- System prompts, structured output, and few-shot examples: Which constraints belong in the prompt, and how will you test their effect?
- Answer evaluation: How will you detect unsupported claims and false refusals?

## Learning Outcomes

- Design and assess answers that cite retrieved evidence rather than relying on model memory.
- Distinguish unanswerable questions from answerable ones with imperfect retrieval.
- Compare prompt versions on a fixed set of questions and record remaining failures.

## Tasks

- Write a prompt that forces answers to rely on retrieved context only, with inline citations.
- Add a refusal path: if context doesn't contain the answer, say so.
- Test with questions that have no answer in the corpus, and questions where retrieved context conflicts.
- Compare 2 to 3 prompt versions on a fixed set of 20 questions, scored by hand.

## Acceptance Criteria

- The system refuses on unanswerable questions in most test cases, without refusing answerable ones.
- Prompt versions are saved with their scores.

## Learning Check

What prompt change made the biggest difference? What kind of hallucination remained?
