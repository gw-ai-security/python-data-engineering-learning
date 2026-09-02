# 08 – pandas for Data Engineering

## Einordnung

pandas wird hier als lokales Transformationswerkzeug gelernt, nicht als Data-Analyst-Spezialisierung.

## DataFrame

```python
import pandas as pd

df = pd.DataFrame([
    {"id": 1, "country": "at", "amount": 10.0},
    {"id": 2, "country": "de", "amount": 20.0},
])
```

Ein DataFrame ist eine tabellarische Datenstruktur mit Zeilen, Spalten und Datentypen.

## Grundoperationen

```python
print(df.dtypes)
clean = df.rename(columns={"amount": "revenue"})
clean = clean[clean["revenue"] > 0]
clean["country"] = clean["country"].str.upper()
```

Weitere Kernbereiche:

- CSV / JSON einlesen
- Spalten auswählen
- umbenennen
- filtern
- Missing Values
- Duplicates
- Sortierung
- Derived Columns
- Date Conversion
- Merge / Join
- passende GroupBy-Transformation
- Output schreiben

## Grain zuerst

Vor der Transformation formulieren:

> One row represents ...

Beispiel: eine Messung pro Station und Timestamp.

## Merge kontrollieren

Nach jedem Merge fragen:

- Welche Zeilenzahl erwarte ich?
- Hat sich der Grain verändert?
- Sind Duplikate entstanden?

## Scale

pandas eignet sich für lokalen / überschaubaren Umfang. Verteilte Verarbeitung kommt später mit PySpark / Databricks.

## Gate

Unbekanntes kleines Dataset: Grain bestimmen, Schema prüfen, bereinigen, Merge durchführen, Row Counts reconciliieren und Output erklären.
