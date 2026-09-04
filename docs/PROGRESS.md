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

**Status:** In progress; major guided practice implemented, formal block gate not yet closed.

Implemented exercises:

1. `01_transaction_validation.py`
   - atomic boolean checks;
   - combined `and` validation.
2. `02_transaction_classification.py`
   - ordered `if / elif / else` rules;
   - first-match behavior.
3. `03_customer_eligibility.py`
   - membership checks;
   - `and`, `or`, `not` concepts in business rules.
4. `04_customer_validation_loop.py`
   - apply rules to multiple records;
   - accepted vs. rejected collections.
5. `05_rejection_reasons.py`
   - multiple independent `if` checks;
   - structured rejection reasons per rejected record.
6. `06_loop_control.py`
   - `continue` skips one record;
   - `break` stops processing;
   - special-case checks must precede broader overlapping conditions.

Remaining according to the operational learning plan:

- `range` and off-by-one behavior;
- `while` and termination conditions;
- boundary-value testing;
- intentionally debug a wrong condition / off-by-one / loop-termination case;
- independent no-AI gate: implement at least five validation rules and split records into accepted/rejected with explainable reasons.

### Block 3 – Data structures

**Status:** Planned / next major block after Block 2 gate.

Target concepts:

- list;
- tuple;
- set;
- dictionary;
- nested structures;
- membership;
- mutation and copying;
- uniqueness;
- choosing a structure based on order, mutability, uniqueness and key/value access.

Note: lists and dictionaries have already appeared in baseline and Block 2 exercises, but Block 3 is where their behavior and trade-offs are studied explicitly.

## Progress rule

The repository README may summarize progress, but this file is the detailed source of truth for implementation evidence. When a new exercise or gate is completed, update this ledger in the same or next documentation commit.
