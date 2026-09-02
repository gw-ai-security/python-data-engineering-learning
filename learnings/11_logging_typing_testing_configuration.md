# 11 – Logging, Typing, Basic Testing, Configuration

## Ziel

Aus einem "funktionierenden Script" wird ein nachvollziehbares Engineering-Artefakt.

## Logging

Nicht überall `print()` als Betriebsbeobachtung verwenden.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("pipeline_started")
```

Sinnvolle Informationen:

- Pipeline Start / Ende
- Run ID
- Source
- Rows received
- Rows valid / rejected
- Rows written
- relevante Errors
- grobe Laufzeit

## Typing

Type Hints machen Funktions-Contracts klarer:

```python
def normalize_country(value: str) -> str:
    return value.strip().upper()
```

Typing ersetzt keine Runtime-Validation.

## Configuration

Trenne:

```text
Code
Configuration
Secrets
```

Config-Beispiele: API Base URL, Zielpfad, Tabellenname, Timeout.  
Secrets: Token, Passwort, Connection Credentials.

## Basic Testing

Pure Transformations und Validation Rules sind besonders gut testbar.

```python
def normalize_country(value):
    return value.strip().upper()


def test_normalize_country():
    assert normalize_country(" at ") == "AT"
```

Wichtige Tests:

- normaler Fall
- Edge Case
- Validation Rule
- Regression für einen früheren Bug
- End-to-End-Smoke-Test

## Regression Test

Wenn ein Bug gefunden und behoben wird, hält ein Regression Test fest, dass derselbe Fehler nicht unbemerkt zurückkommt.

## Gate

Bestehende Mini-Pipeline mit Logging, zentralen Type Hints, getrennter Config, mehreren sinnvollen Tests und mindestens einem Regression Test ausstatten.
