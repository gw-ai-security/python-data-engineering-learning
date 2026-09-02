# 04 – Functions, Modules, Comprehensions, Code Structure

## Wozu dient das?

Eine Pipeline soll nicht aus einem 300-Zeilen-Script bestehen. Funktionen zerlegen Logik in benannte Verantwortlichkeiten und machen Tests und Debugging einfacher.

## Functions

```python
def clean_country(value):
    return value.strip().upper()
```

- Parameter = Input
- `return` = Output
- Scope = wo Variablen sichtbar sind

`print()` zeigt etwas an; `return` gibt einen Wert an den aufrufenden Code zurück.

## Klare Verantwortlichkeiten

```python
def extract(): ...
def validate(records): ...
def clean(records): ...
def transform(records): ...
def load(records): ...
def run_pipeline(): ...
```

## Modules

Eine `.py`-Datei kann als Modul importiert werden:

```python
from validation import validate_record
```

Das erlaubt strukturierte Dateien statt eines Monolithen.

## Comprehensions

Kompakte Transformationen sind nützlich, solange sie lesbar bleiben:

```python
active_ids = [r["id"] for r in records if r["active"]]
```

Nicht jede Schleife muss in eine Comprehension umgebaut werden.

## Qualitätsfragen pro Funktion

- Was ist Input?
- Was ist Output?
- Welche Side Effects gibt es?
- Welche Fehler sind möglich?
- Wie teste ich sie isoliert?

## Data-Engineering-Transfer

Eine Cleaning-Aufgabe in Module und Funktionen zerlegen. Fachlogik soll nicht gleichzeitig API, DB und Logging erledigen.

## Recall

- `print` vs. `return`?
- Warum kleine Funktionen?
- Wann wird eine Funktion zu groß?
- Was ist ein Modul?
- Warum hilft Separation of Concerns beim Testen?

## Gate

Ein früheres Script refactoren: keine Copy-Paste-Duplikate, klare Funktionen, mindestens zwei Module und unverändertes fachliches Ergebnis.
