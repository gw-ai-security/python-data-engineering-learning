# 05 – Errors, Exceptions, Datetime, Regex, Debugging

## Wozu dient das?

Daten und externe Systeme sind unzuverlässig. Eine Pipeline muss unterscheiden können, ob ein Record schlecht ist oder der gesamte Lauf abbrechen soll.

## Häufige Fehler

- `SyntaxError`
- `TypeError`
- `ValueError`
- `KeyError`
- `FileNotFoundError`

## Exceptions

```python
try:
    quantity = int(raw_quantity)
except ValueError:
    quantity = None
```

Spezifische Exceptions sind besser als blind alles zu fangen.

```python
try:
    ...
except ValueError:
    ...
else:
    ...
finally:
    ...
```

Mit `raise` kann Code bewusst einen Fehler signalisieren.

## Validation vs. Exception Handling

Validation fragt vorher: "Ist der Wert erlaubt?"  
Exception Handling reagiert darauf, dass eine Operation tatsächlich fehlschlägt.

Nicht jedes Problem soll mit `try/except` versteckt werden.

## Datetime

```python
from datetime import datetime

ts = datetime.strptime("2026-09-02", "%Y-%m-%d")
```

Date Parsing ist in Pipelines häufig, weil Quellen unterschiedliche Formate liefern.

## Regex

Regex nur verwenden, wenn Parsing / Validation es wirklich braucht. Für einfache String-Aufgaben sind normale String-Methoden meist lesbarer.

## Debugging

```text
Expected → Actual → Hypothesis → Minimal Reproduction → Fix → Verify → Prevent
```

## Failure Policy

Bei Fehlern bewusst entscheiden:

- Pipeline abbrechen?
- Record ablehnen?
- Default setzen?
- loggen und fortfahren?

## Recall

- Exception Handling vs. Validation?
- Warum spezifische Exceptions?
- Wann `raise`?
- Warum ist `except Exception: pass` gefährlich?

## Gate

Einen unbekannten Stack Trace ohne AI analysieren und die Ursache lokalisieren.
