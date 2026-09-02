# 09 – Data Quality and Schema Validation

## Wozu dient das?

Data Quality ist kein kosmetischer Check nach der Pipeline. Qualitätsregeln sind Teil des Contracts zwischen Quelle, Pipeline und Consumer.

## Qualitätsdimensionen

- **Completeness** – Pflichtwerte vorhanden?
- **Uniqueness** – Schlüssel eindeutig?
- **Validity** – Werte im erlaubten Bereich / Format?
- **Consistency** – Regeln widerspruchsfrei?
- **Timeliness** – Daten aktuell genug?
- **Referential Integrity** – Referenzen gültig?

## Dataset Contract

Für jedes Dataset definieren:

```text
Grain
Required Fields
Business / Primary Key
Datentypen
erlaubte Werte
Range Rules
Date Rules
Duplicate Rules
Referenzen
Freshness
Failure Policy
```

Beispiel:

```python
def is_valid(record):
    return (
        record.get("id") is not None
        and isinstance(record.get("amount"), (int, float))
        and record["amount"] >= 0
    )
```

## Accepted / Rejected

```text
received_rows
├── valid_rows
└── rejected_rows
```

Ein DQ Report kann zusätzlich Duplicate-, Null- und Validity-Verstöße zählen.

## Grain

Ohne Grain ist kaum prüfbar, ob Duplikate wirklich Duplikate sind.

## Failure Policy

Nicht jede Verletzung bedeutet Pipeline-Abbruch. Manche Records werden abgelehnt, andere Fehler machen den gesamten Batch unbrauchbar.

## Gate

Mindestens fünf DQ-Regeln aus einer kurzen Business-Spezifikation selbst ableiten, implementieren und bewusst schlechte Daten korrekt klassifizieren.
