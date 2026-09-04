# Exercises

Focused coding exercises and no-AI practice organized by the operational learning blocks.

```text
exercises/
├── 00_setup_baseline/
├── 01_execution_variables_types_strings_numbers/
├── 02_booleans_operators_conditions_loops/
├── 03_data_structures/
├── 04_functions_modules_code_structure/
├── 05_errors_exceptions_datetime_regex_debugging/
├── 06_files_pathlib_json_csv_config/
├── 07_http_rest_api_ingestion/
├── 08_pandas_data_engineering/
├── 09_data_quality_schema_validation/
├── 10_postgresql_sql_parquet/
├── 11_logging_typing_testing_configuration/
└── 12_mini_pipeline_rehearsal/
```

Theory belongs in [`../learnings/`](../learnings/). Detailed progress evidence belongs in [`../docs/PROGRESS.md`](../docs/PROGRESS.md).

## Current exercise inventory — 2026-09-04

### `00_setup_baseline/`

Contains the pre-learning sequence plus the baseline challenge that combined lists, dictionaries, loops, conditions, type checks, filtering and aggregation.

### `01_execution_variables_types_strings_numbers/`

Implemented:

```text
01_string_normalization.py
02_string_extraction.py
03_type_casting.py
04_numeric_operations.py
05_float_precision.py
06_parse_raw_record.py
07_string_validation.py
```

Guided exercise set: complete. Independent Block-1 gate: not yet recorded.

### `02_booleans_operators_conditions_loops/`

Implemented:

```text
01_transaction_validation.py
02_transaction_classification.py
03_customer_eligibility.py
04_customer_validation_loop.py
05_rejection_reasons.py
06_loop_control.py
```

Still required before the formal Block-2 gate is closed:

- `range` and off-by-one practice;
- `while` and termination-condition practice;
- explicit boundary-value debugging;
- independent validation/rejection gate.

### `03_data_structures/`

Planned next major block after Block 2 is formally closed.

## Exercise rules

- Write the first solution yourself before using AI review where possible.
- Keep exercises small enough that the concept being practiced is obvious.
- Preserve useful failed attempts only when they teach a debugging lesson; otherwise keep the final script readable.
- Use English identifiers and clear names.
- Comments should explain intent, assumptions or non-obvious logic rather than restating every line.
- Keep learner-authored exercise code as evidence; polished production abstractions belong later in mini-projects or pipeline code.
- Empty future directories may use `.gitkeep`; once a directory contains real files, `.gitkeep` is no longer needed.
