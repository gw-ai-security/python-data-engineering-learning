# Learning Method

## Core loop

```text
UNDERSTAND → RECALL → IMPLEMENT → BREAK → DEBUG → TEST → EXPLAIN → INTEGRATE → DOCUMENT → PROVE
```

The purpose is to build usable engineering competence, not course-completion evidence.

## Brain First → AI Second → Brain Again

In learning mode:

1. Read the task.
2. Structure the problem yourself.
3. Start without AI.
4. Observe failures and form a hypothesis.
5. Use AI as tutor or reviewer only after genuine effort.
6. Verify the suggestion.
7. Correct the solution yourself.
8. Reproduce the skill later without AI.

Good AI uses: code review, edge cases, test ideas, refactoring, stack-trace explanation and alternatives.

Bad default: task → AI → copy code → assume understanding.

## Evidence states

Repository progress uses explicit evidence states:

- **Planned** – the topic exists in the roadmap.
- **Guided practice** – the concept has been implemented with tutor/reviewer support.
- **Independent gate pending** – guided exercises exist, but independent reproduction has not yet been recorded.
- **Gate passed** – the defined task can be implemented, explained and debugged without step-by-step help.
- **Integrated** – the skill is reused inside a larger mini-project or pipeline.

This distinction is important because successful guided code is evidence of progress, but not yet proof of independent competence.

The current evidence ledger is [`PROGRESS.md`](PROGRESS.md).

## Confusion Compass

Turn vague confusion into a precise question.

Bad:

> Exceptions are confusing.

Better:

- Why validate before execution in one case but catch an exception in another?
- When should one bad record be rejected instead of aborting the batch?
- Why does this JSON become a dict instead of a list?

Then answer the question and apply the answer in code.

## Debugging protocol

```text
OBSERVE → HYPOTHESIZE → ISOLATE → TEST → FIX → VERIFY → PREVENT
```

For meaningful bugs:

- expected behavior;
- actual behavior;
- hypothesis;
- minimal reproduction;
- relevant stack trace / logs / input data;
- fix;
- verification;
- regression test where useful.

Debugging evidence matters. A corrected program is more valuable when the learner can explain what failed, why the hypothesis was plausible and how the fix was verified.

## Concept first, tool second

Examples:

- understand HTTP request/response before learning a requests library;
- understand dependency isolation before using `venv` and pip;
- understand tabular transformation before relying on pandas;
- understand relational persistence before choosing a PostgreSQL driver.

## Separation of Concerns

A pipeline stage should have one clear responsibility:

```text
Extract   → obtain data
Raw       → preserve source
Validate  → check structure and rules
Clean     → standardize
Transform → apply business logic
Load      → persist
Logging   → operational evidence
Config    → changeable parameters
Tests     → verify behavior
```

Avoid one function that downloads an API response, cleans it, applies business rules and writes the database at the same time.

## Definition of Done

- **Level 1 – Explain**
- **Level 2 – Implement**
- **Level 3 – Debug**
- **Level 4 – Reason / Operate**

Fundamentals and pipeline-core topics should mainly reach Levels 2–3 in this phase.

A block should only be described as complete when its gate is supported by actual repository evidence, not merely by a completed video section or guided exercise count.
