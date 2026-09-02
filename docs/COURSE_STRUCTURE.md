# Course Structure

This document stores the operational structure of the Python Data Engineering learning phase.

## 1. Primary conceptual course: Data with Baraa

The fundamentals are organized as **thinking layers**, not as isolated syntax chapters:

1. Foundations
2. Strings and Numbers
3. Boolean / Operators
4. Conditions
5. Loops
6. Data Structures
7. Functions

The central idea is to understand how Python works with data, execution flow, decisions, collections and reusable logic instead of memorizing syntax.

## 2. Practice source: 30 Days of Python – re-sequenced

The exercise source is not followed as a rigid 30-day streak. It is re-sequenced for Data Engineering.

### Priority A – required

- Day 01 – Introduction
- Day 02 – Variables, Built-in Functions
- Day 03 – Operators
- Day 04 – Strings
- Day 05 – Lists
- Day 06 – Tuples
- Day 07 – Sets
- Day 08 – Dictionaries
- Day 09 – Conditionals
- Day 10 – Loops
- Day 11 – Functions
- Day 12 – Modules
- Day 13 – List Comprehension
- Day 15 – Python Type Errors
- Day 16 – Python Date Time
- Day 17 – Exception Handling
- Day 18 – Regular Expressions, selectively for parsing / validation
- Day 19 – File Handling
- Day 20 – Package manager + requests / API basics
- Day 23 – Virtual Environment
- Day 25 – pandas
- Day 28 – API / HTTP

**Sequence change:** Virtual environments are moved to the beginning of the learning plan.

### Priority B – selective

- Day 14 – Higher Order Functions: understand basic `map`, `filter`, `lambda`; no functional-programming specialization.
- Day 21 – Classes and Objects: understand class, object and constructor; use only when it improves responsibilities and readability.

### Priority C – optional / later

- Day 22 – Web Scraping only for a concrete ingestion use case.
- Day 24 – Statistics is not a current Data Engineering bottleneck.

### Priority D – deliberately deferred

- Day 26 – Python Web
- Day 27 – MongoDB
- Day 29 – Building an API
- Day 30 – Conclusions

The current target stack prioritizes PostgreSQL and consuming APIs, not web-development or MongoDB specialization.

## 3. Operational learning blocks

### Block 0 – Setup, workflow and baseline
Professional project environment, `.venv`, pip, requirements, Git, VS Code, project layout and baseline diagnosis.

### Block 1 – Execution, variables, types, strings, numbers
Variables, `int`, `float`, `str`, `bool`, `None`, casting, string normalization, slicing, f-strings and numeric operations.

### Block 2 – Booleans, operators, conditions, loops
Validation logic, comparisons, `and/or/not`, `if/elif/else`, `for`, `while`, `break`, `continue`, `range` and boundary conditions.

### Block 3 – Data structures
Lists, tuples, sets, dictionaries, nested structures, membership, mutation, uniqueness and choosing the correct structure for a data problem.

### Block 4 – Functions, modules and code structure
Functions, parameters, return values, scope, modules, imports, comprehensions and Separation of Concerns.

### Block 5 – Errors, exceptions, datetime, regex, debugging
Common Python errors, specific exceptions, `try/except`, `raise`, date parsing, selective regex use and systematic stack-trace analysis.

### Block 6 – Files, pathlib, JSON, CSV, packages, config
Local file pipelines, JSON / CSV, `pathlib`, `with`, pip, requirements, environments, configuration and secrets hygiene.

### Block 7 – HTTP and REST API ingestion
Client/server model, requests, responses, status codes, timeouts, pagination, rate limits, retry concepts and raw response persistence.

### Block 8 – pandas for Data Engineering
Local tabular transformations, schema inspection, dtypes, nulls, duplicates, merges, grain and reconciliation.

### Block 9 – Data Quality and schema validation
Completeness, uniqueness, validity, consistency, timeliness, referential integrity, contracts, accepted/rejected records and DQ summaries.

### Block 10 – PostgreSQL, SQL and Parquet
Database connections, parameterized SQL, transactions conceptually, insert/upsert thinking, row-count reconciliation and Parquet output.

### Block 11 – Logging, typing, basic testing, configuration
Move from a working script to an engineering artifact with structured logs, clear function contracts, separated config and meaningful tests.

### Block 12 – Mini-pipeline rehearsal
No-tutorial integration gate: API → raw JSON → validation → standardization → transformation → PostgreSQL + Parquet → DQ → logging → tests.

## 4. Learning session structure

A typical session follows:

1. **Active Recall – 10–15 min**
2. **Theory – max. ~20%**
3. **Coding – ~50–60%**
4. **Data Engineering transfer – ~20–30%**
5. **Close – commit, confusion questions, debugging insight**

## 5. Final phase gate

Before the portfolio project begins, the mini-pipeline must work without tutorial guidance and must be debuggable.

The final project is then:

```text
PUBLIC REST API
→ RAW JSON
→ VALIDATION
→ CLEAN / STANDARDIZED DATA
→ BUSINESS TRANSFORMATION
→ POSTGRESQL + PARQUET
→ DATA QUALITY + LOGGING + TESTS
```
