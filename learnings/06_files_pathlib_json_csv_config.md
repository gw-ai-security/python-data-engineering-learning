# 06 – Files, pathlib, JSON, CSV, Packages, Config

## Wozu dient das?

Data Engineering bewegt Daten zwischen Quellen und Zielen. Lokale Dateien sind die einfachste Umgebung, um Ingestion, Raw-Sicherung, Cleaning und Output zu lernen.

## `pathlib`

```python
from pathlib import Path

raw_path = Path("data/raw/input.json")
```

`pathlib` ist lesbarer und portabler als viele hart codierte Pfadstrings.

## Dateien mit Context Manager

```python
with open(raw_path, "r", encoding="utf-8") as file:
    text = file.read()
```

`with` sorgt dafür, dass die Ressource sauber geschlossen wird.

## JSON

```python
import json

with open(raw_path, encoding="utf-8") as file:
    payload = json.load(file)
```

- JSON object → meist Python `dict`
- JSON array → meist Python `list`

Schreiben:

```python
with open("data/clean/output.json", "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2)
```

## CSV

CSV ist tabellarisch, aber Typen sind nicht automatisch zuverlässig. Schema und Encoding müssen bewusst behandelt werden.

## Landing Zone

```text
data/
├── raw/
├── clean/
└── curated/
```

Raw bleibt möglichst unverändert, damit Reprocessing und Debugging möglich bleiben.

## Config und Secrets

Code, Konfiguration und Secrets trennen. Keine Tokens oder DB-Passwörter committen.

## Recall

- Warum `with open`?
- JSON string vs. Python dict?
- Warum Raw-Daten erhalten?
- Warum `pathlib`?
- Was gehört nicht ins Git-Repo?

## Gate

Eine kleine File-Pipeline von raw JSON zu validiertem JSON/CSV aus einem leeren Ordner aufbauen.
