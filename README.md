# Python Data Engineering Learning

Hands-on learning repository for building reliable Python skills for Data Engineering.

This repository is not designed around course completion. It is designed around demonstrable engineering competence: understanding, implementing, debugging, testing, explaining, and integrating Python into a reliable local data pipeline.

## Target outcome

The Python phase culminates in an independently built pipeline:

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

The project intentionally does **not** start with Airflow, dbt, AWS, Spark, Databricks or Kubernetes. The local Python system must first be understandable, reproducible, testable and debuggable.

## Learning principles

The working model is:

```text
UNDERSTAND
→ RECALL
→ IMPLEMENT
→ BREAK
→ DEBUG
→ TEST
→ EXPLAIN
→ INTEGRATE
→ DOCUMENT
→ PROVE
```

Key rules:

- one primary technical learning goal at a time;
- roughly 20% theory / 80% active work;
- Brain First → AI Second → Brain Again;
- debugging is a core skill, not a side effect;
- concept first, tool second;
- Data Engineering transfer for every Python topic;
- separation of concerns in pipeline code;
- GitHub evidence matters more than course certificates.

## Repository structure

```text
python-data-engineering-learning/
├── README.md
├── docs/
│   ├── COURSE_STRUCTURE.md
│   ├── LEARNING_METHOD.md
│   └── SOURCE_MAP.md
├── learnings/
│   ├── README.md
│   ├── 00_setup_baseline.md
│   ├── 01_execution_variables_types_strings_numbers.md
│   ├── 02_booleans_operators_conditions_loops.md
│   ├── 03_data_structures.md
│   ├── 04_functions_modules_code_structure.md
│   ├── 05_errors_exceptions_datetime_regex_debugging.md
│   ├── 06_files_pathlib_json_csv_config.md
│   ├── 07_http_rest_api_ingestion.md
│   ├── 08_pandas_data_engineering.md
│   ├── 09_data_quality_schema_validation.md
│   ├── 10_postgresql_sql_parquet.md
│   ├── 11_logging_typing_testing_configuration.md
│   └── 12_mini_pipeline_rehearsal.md
├── exercises/
├── mini_projects/
├── notes/
├── tests/
├── requirements.txt
├── .editorconfig
├── .gitignore
└── .vscode/
```

### What belongs where?

- **`learnings/`** – concise theory, mental models, examples, code snippets and recall questions for every learning block.
- **`exercises/`** – code written during focused practice and no-AI gates.
- **`mini_projects/`** – small integrated Data Engineering exercises.
- **`tests/`** – automated tests as testing becomes part of the learning path.
- **`notes/`** – personal confusion questions, debugging observations and short reflections.
- **`docs/`** – course structure, learning method and source mapping.

## Learning blocks

| Block | Focus |
|---|---|
| 0 | Setup, workflow and baseline |
| 1 | Python execution, variables, types, strings, numbers |
| 2 | Booleans, operators, conditions, loops |
| 3 | Lists, tuples, sets, dictionaries |
| 4 | Functions, modules, comprehensions, code structure |
| 5 | Errors, exceptions, datetime, regex, debugging |
| 6 | Files, pathlib, JSON, CSV, packages, configuration |
| 7 | HTTP and REST API ingestion |
| 8 | pandas for Data Engineering |
| 9 | Data Quality and schema validation |
| 10 | PostgreSQL, SQL from Python and Parquet |
| 11 | Logging, typing, basic testing, configuration |
| 12 | Mini-pipeline rehearsal / no-tutorial gate |

See [`docs/COURSE_STRUCTURE.md`](docs/COURSE_STRUCTURE.md) for the full sequence and [`learnings/`](learnings/) for readable theory notes.

## Definition of Done

A topic is not considered learned because it appeared in a video or because code ran once.

**Level 1 – Explain**  
Explain the purpose and basic mechanics.

**Level 2 – Implement**  
Solve a typical task without a step-by-step tutorial.

**Level 3 – Debug**  
Locate and fix common failures systematically.

**Level 4 – Reason / Operate**  
Explain trade-offs, failure modes, security, tests, logging and operational consequences.

For this Python phase, fundamentals and the pipeline core should reach mainly Levels 2–3.

## Debugging workflow

```text
OBSERVE
→ HYPOTHESIZE
→ ISOLATE
→ TEST
→ FIX
→ VERIFY
→ PREVENT
```

For relevant bugs, record expected behavior, actual behavior, hypothesis, minimal reproduction, fix and verification. Add a regression test where useful.

## Current status

- Python 3.14 environment established with a project-local `.venv`.
- Setup and baseline exercises completed.
- Next phase: Block 1 – Python execution, variables, types, strings and numbers.

## Final project

The final Python-phase project is the **Reliable Local Data Pipeline**:

```text
API → Python → Validation → PostgreSQL + Parquet → Data Quality → Logging → Tests
```

Before implementation, the project must define the problem, consumer, source, grain, valid record rules, business rules, expected failures and Definition of Done.

## Scope discipline

The following are deliberately deferred until the Python pipeline itself is reliable:

- dbt
- Airflow
- Docker / CI/CD depth
- AWS
- PySpark
- Databricks
- advanced distributed processing

## License

MIT License.

## Author

Georg Wiesmüller  
Business Informatics student focused on Data Engineering and the long-term intersection of reliable data platforms, security and AI governance.
