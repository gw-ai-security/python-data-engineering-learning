# Progress & Evidence Ledger

This file tracks what has actually been implemented in the repository. It deliberately distinguishes guided practice from independent competence gates.

## Status model

- **Planned** – documented in the roadmap, no coding evidence yet.
- **Guided practice** – concept implemented in exercises with tutor/reviewer support.
- **Independent gate pending** – the exercise set exists, but no no-template/no-AI reproduction has been recorded yet.
- **Gate passed** – the block's defined task can be reproduced independently and explained/debugged.
- **Integrated** – the skill is reused inside a larger mini-project or pipeline.

This prevents a common error: equating “I wrote the exercise once” with “I can reliably use the skill.”

## Current snapshot — 2026-09-04

### Block 0 – Setup, workflow and baseline

**Status:** Operational; formal dependency checkpoint deferred.

Evidence:

- project-local `.venv` created and used;
- Python scripts executed from PowerShell / VS Code terminal;
- Git repository and structured learning workspace established;
- baseline challenge implemented after pre-learning;
- `.gitignore`, `.editorconfig`, VS Code settings and `requirements.txt` exist;
- `requirements.txt` intentionally contains no third-party runtime packages yet.

Remaining before the strict source-plan gate can be called fully evidenced:

- install the first genuinely required third-party package inside `.venv`;
- record/freeze the dependency in the project requirements workflow;
- explain the dependency path and environment isolation without prompting.

### Block 1 – Python execution, variables, types, strings, numbers

**Status:** Guided practice complete; independent gate pending.

Implemented exercises:

1. `01_string_normalization.py`
   - `.strip()`, `.title()`, `.upper()`;
   - raw vs. cleaned values;
   - field-specific normalization rules.
2. `02_string_extraction.py`
   - indexing and slicing;
   - extracting structured parts from a code.
3. `03_type_casting.py`
   - `str → int`, `str → float`;
   - identifier semantics vs. numeric measures.
4. `04_numeric_operations.py`
   - arithmetic with `int` and `float`;
   - type propagation.
5. `05_float_precision.py`
   - binary floating-point precision caveat.
6. `06_parse_raw_record.py`
   - delimiter split;
   - trim, normalize, cast and calculate from one raw record.
7. `07_string_validation.py`
   - `.isdigit()`, `.isalpha()`, `.startswith()`, `.endswith()`;
   - transformation vs. validation.

Important learned constraints:

- a numeric-looking identifier may need to stay a string because arithmetic has no business meaning and leading zeros can be significant;
- `.title()` is a simple normalization rule, not a universally correct person-name normalizer;
- `float` is not an exact decimal representation and should not be blindly treated as financial arithmetic;
- raw source values should not be overwritten without a deliberate reason.

Remaining gate:

- independently normalize a small set of messy raw fields without step-by-step guidance and explain each assumption.

### Block 2 – Booleans, operators, conditions, loops

**Status:** **Gate passed — 2026-09-04.**

Implemented exercises:

1. `01_transaction_validation.py`
   - atomic boolean checks;
   - combined `and` validation.
2. `02_transaction_classification.py`
   - ordered `if / elif / else` rules;
   - first-match behavior.
3. `03_customer_eligibility.py`
   - membership checks;
   - `and`, `or`, `not` in business rules.
4. `04_customer_validation_loop.py`
   - apply rules to multiple records;
   - accepted vs. rejected collections.
5. `05_rejection_reasons.py`
   - multiple independent `if` checks;
   - structured rejection reasons per rejected record.
6. `06_loop_control.py`
   - `continue` skips one record;
   - `break` stops processing;
   - specific stop conditions precede broader overlapping rules.
7. `07_range_and_boundaries.py`
   - `range(start, stop)` and exclusive stop semantics;
   - inclusive business boundaries via `max_page + 1`;
   - off-by-one awareness.
8. `08_while_loop.py`
   - state-controlled iteration;
   - pagination-style loops;
   - retry-style loops;
   - explicit termination through state mutation.
9. `09_debug_loop_conditions.py`
   - boundary-condition debugging;
   - infinite-loop root cause analysis;
   - OBSERVE → HYPOTHESIZE → ISOLATE → TEST → FIX → VERIFY → PREVENT.
10. `10_independent_gate.py`
    - five independent validation rules;
    - accepted/rejected split;
    - all rejection reasons captured structurally;
    - accepted/rejected counts;
    - no function abstraction or step-by-step solution template.

Independent gate evidence:

```text
TX-001 → accepted
TX-002 → rejected: amount <= 0
TX-003 → rejected: country outside Austria/Germany
TX-004 → rejected: inactive customer
TX-005 → rejected: blocked customer
```

The gate demonstrates that the learner can independently:

- translate business rules into named Boolean checks;
- combine and invert conditions correctly;
- use independent `if` statements when multiple reasons may coexist;
- process a collection record by record;
- store validation evidence in structured lists/dictionaries;
- reason about `range` boundaries and `while` termination;
- debug an off-by-one error and a non-terminating loop.

Next competence step: reuse these control-flow skills inside Block 3 data-structure work and later integrated pipeline exercises.

### Block 3 – Data structures

**Status:** Next active block; formal exercise evidence not yet recorded.

Target concepts:

- list mutation and copying/reference behavior;
- tuple;
- set;
- dictionary operations;
- nested structures;
- membership;
- mutability and copying;
- uniqueness;
- choosing a structure based on order, mutability, uniqueness and key/value access.

Note: lists and dictionaries have already appeared in baseline and Block 2 exercises, but Block 3 studies their behavior and trade-offs explicitly.

First planned exercise: understand why assigning one list variable to another does not create an independent copy, then implement a safe copy for the intended use case.

## Progress rule

The repository README may summarize progress, but this file is the detailed source of truth for implementation evidence. When a new exercise or gate is completed, update this ledger in the same or next documentation commit.
