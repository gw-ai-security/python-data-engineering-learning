# Python Data Engineering Learning

Hands-on learning repository for building practical Python skills for Data Engineering.

The goal is not to collect Python syntax or finish courses for their own sake. The goal is to build enough Python engineering competence to independently implement, test, debug, explain, and later operate a reliable local data pipeline.

## Target Outcome

This learning phase culminates in an end-to-end local pipeline:

```text
Public REST API
        ↓
Raw JSON
        ↓
Validation
        ↓
Clean / Standardized Data
        ↓
Business Transformation
        ↓
PostgreSQL + Parquet
        ↓
Data Quality
        ↓
Logging + Tests
```

The project intentionally starts without Airflow, dbt, Docker, AWS, Spark, Databricks, or Kubernetes. The Python pipeline itself must first be understandable, reproducible, testable, and debuggable.

## Learning Method

The repository follows a practice-first workflow:

```text
Understand
→ Recall
→ Implement
→ Break
→ Debug
→ Test
→ Explain
→ Integrate
→ Document
→ Prove
```

Core rules:

- approximately 20% learning material and 80% coding;
- exercises are attempted before AI assistance;
- AI is used primarily for review, feedback, edge cases, refactoring, and explanation;
- debugging is treated as a core engineering skill;
- readable and maintainable Python is preferred over unnecessary complexity;
- every topic is connected to a Data Engineering use case.

## Current Phase

**Learning Block 0 — Setup, workflow, and baseline**

Current objectives:

- execute Python from the terminal;
- work with `.py` files in VS Code;
- understand system Python vs. project environment;
- create and activate a virtual environment;
- manage dependencies with `pip` and `requirements.txt`;
- use Git and GitHub as part of the normal workflow;
- complete an initial no-AI baseline challenge.

### Learning Block 0 Gate

The block is complete when I can independently:

- create and activate a virtual environment;
- install a package into the project environment;
- generate/update `requirements.txt`;
- execute a Python script from the terminal;
- create a Git commit;
- explain why a virtual environment is used.

## Repository Structure

```text
python-data-engineering-learning/
├── .vscode/          # Minimal VS Code workspace configuration
├── exercises/        # Focused Python exercises and no-AI practice
├── mini_projects/    # Applied Data Engineering exercises
├── notes/            # Concise learning notes and debugging observations
├── tests/            # Automated tests introduced as the roadmap progresses
├── .editorconfig     # Basic cross-editor formatting rules
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

The structure will evolve only when a learning block or project creates a real need for additional folders.

## Learning Path

1. Setup, workflow, and baseline
2. Python execution, variables, types, strings, and numbers
3. Booleans, operators, conditions, and loops
4. Lists, tuples, sets, and dictionaries
5. Functions, modules, and packages
6. Files, CSV, JSON, and `pathlib`
7. Exceptions and defensive programming
8. HTTP and REST APIs
9. pandas for local transformations
10. Data quality and schema validation
11. PostgreSQL, SQL from Python, and Parquet
12. Logging, typing, basic testing, and configuration
13. Reliable local Data Engineering pipeline

## Definition of Done

A skill is not considered learned because it appeared in a course.

**1. Explain**  
Describe the purpose and behavior of the concept.

**2. Implement**  
Solve a typical task without a step-by-step tutorial.

**3. Debug**  
Systematically locate and fix typical failures.

**4. Reason about / operate**  
Explain assumptions, trade-offs, failure modes, security, logging, tests, and operational consequences where relevant.

For Python fundamentals, the target during this phase is primarily levels 2–3.

## Debugging Workflow

```text
Observe
→ Hypothesize
→ Isolate
→ Test
→ Fix
→ Verify
→ Prevent
```

Relevant errors are kept as learning evidence when they reveal a useful failure mode or lead to a regression test.

## Local Setup — Windows / VS Code

### 1. Clone the repository

```powershell
git clone https://github.com/gw-ai-security/python-data-engineering-learning.git
cd python-data-engineering-learning
```

### 2. Create the project environment

```powershell
py -m venv .venv
```

### 3. Activate it in PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Verify the interpreter and pip

```powershell
python --version
python -m pip --version
```

The `pip` path should point into this repository's `.venv` directory.

### 5. Install project dependencies

At the start of Learning Block 0 there are intentionally no runtime dependencies. When dependencies are introduced:

```powershell
python -m pip install -r requirements.txt
```

The virtual environment itself is local-only and is excluded by `.gitignore`.

## Baseline Challenge

The first diagnostic challenge is completed without AI-generated solution code:

1. create five records as dictionaries;
2. identify invalid records;
3. filter valid records;
4. calculate the sum of one numeric field;
5. print the result as readable text.

The challenge is a diagnostic baseline, not an exam. Gaps become inputs for the following learning blocks.

## Final Python Phase Project

The final project of this phase is expected to demonstrate:

- REST API extraction;
- raw JSON persistence;
- validation and standardization;
- business transformations;
- PostgreSQL loading;
- Parquet output;
- data-quality checks;
- controlled error handling;
- logging;
- basic automated tests;
- reproducible execution;
- technical documentation.

## Scope Boundaries

The following technologies are deliberately deferred until the local Python pipeline is reliable:

- dbt;
- Airflow;
- Docker;
- CI/CD;
- AWS;
- PySpark;
- Databricks.

This keeps the current learning bottleneck explicit: practical Python, debugging, testing, and reliable pipeline logic.

## License

This project is licensed under the MIT License.

## Author

**Georg Wiesmüller**  
Business Informatics student focused on Data Engineering and the long-term intersection of data platforms, security, and AI governance.
