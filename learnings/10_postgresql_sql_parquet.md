# 10 – PostgreSQL, SQL from Python and Parquet

## Wozu dient das?

Nach Validierung und Transformation müssen Daten zuverlässig persistiert und anschließend unabhängig geprüft werden.

## PostgreSQL-Verbindung – Konzept

```text
Python
→ Connection
→ parameterized SQL
→ Transaction
→ PostgreSQL table
```

Credentials gehören in Environment / Config, nicht in den Code.

## Parameterisiertes SQL

Das konkrete Placeholder-Format hängt vom gewählten Treiber ab. Das Prinzip ist wichtig: Werte werden nicht per String-Konkatenation in SQL eingebaut.

Schlecht:

```python
sql = "INSERT INTO sales VALUES (" + user_input + ")"
```

Besser: SQL und Werte getrennt an den Treiber übergeben.

## Transactions

Eine Transaction gruppiert zusammengehörige DB-Änderungen. Fehler sollen nicht zu einem halb geschriebenen fachlichen Zustand führen.

## Insert / Upsert

- Insert: neuen Datensatz schreiben
- Upsert: abhängig vom Schlüssel insert oder update

Die konkrete Strategie hängt vom Ladeverhalten und Business Key ab.

## Parquet

Parquet ist ein spaltenorientiertes analytisches Dateiformat. Es ist für strukturierte analytische Daten wesentlich geeigneter als viele rohe Textformate.

## Reconciliation

Nach dem Load vergleichen:

```text
Python row count
PostgreSQL row count
Parquet row count
```

Zusätzlich eine zentrale Aggregation in Python und SQL gegeneinander prüfen.

## Security

- keine Credentials im Code
- kein SQL aus unvalidiertem String-Input bauen

## Gate

Validated Records sicher in PostgreSQL schreiben, mit SQL verifizieren und denselben fachlichen Output als Parquet erzeugen.
