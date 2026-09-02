# 12 – Mini-Pipeline Rehearsal / No-Tutorial Gate

## Ziel

Vor dem Portfolio-Projekt beweisen, dass die einzelnen Bausteine integriert werden können.

Die erste Implementierung erfolgt ohne Kursvideo und ohne AI-Codegenerierung.

## Aufgabe

Eine kleine öffentliche REST API auswählen und folgende Pipeline bauen:

```text
API
→ GET
→ RAW JSON speichern
→ Records extrahieren
→ Schema / Required Fields validieren
→ ungültige Records separieren
→ Daten standardisieren
→ kleine Business Transformation
→ Parquet schreiben
→ PostgreSQL schreiben
→ DQ Summary
→ Logging
→ Tests
```

## Vor Coding

Eine einseitige Specification schreiben:

- Problem / Consumer
- Source
- Grain
- Required Fields
- Valid Record
- Business Rules
- Module / Functions
- Failure Modes
- Definition of Done

## Beispiel-Moduldenken

```text
extract.py
validate.py
transform.py
load_postgres.py
load_parquet.py
quality.py
main.py
```

Die konkrete Struktur muss sinnvoll sein; sie wird nicht nur wegen eines Musters erzeugt.

## Failure Modes

Mindestens bedenken:

- Request schlägt fehl
- Response leer
- JSON-Struktur unerwartet
- einzelne Records ungültig
- DB nicht erreichbar
- Ziel-Datei nicht schreibbar
- Retry / erneuter Lauf

## AI-Regel

Erste Umsetzung ohne AI. Danach darf AI als Reviewer für Tests, Edge Cases und Refactoring eingesetzt werden.

## Gate

Erst wenn diese Mini-Pipeline ohne Tutorial funktioniert und systematisch debuggt werden kann, beginnt das Abschlussprojekt **Reliable Local Data Pipeline**.
