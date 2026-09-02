# 00 – Setup, Arbeitsweise und Baseline

## Wozu dient dieser Block?

Bevor Code komplex wird, braucht jedes Projekt eine reproduzierbare Umgebung. Ziel ist, System-Python und Projekt-Python zu trennen und sicher mit Git, VS Code, `venv` und pip zu arbeiten.

## Virtual Environment

Ein `venv` isoliert die Packages eines Projekts.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip --version
```

Nach Aktivierung sollte der pip-Pfad innerhalb von `.venv` liegen.

Mental Model:

```text
Windows
├── System Python
└── Project
    └── .venv
        ├── Python
        └── Packages
```

## Warum `python -m pip`?

Damit wird pip mit genau dem Python-Interpreter ausgeführt, den du gerade verwendest.

## Was gehört nicht in Git?

- `.venv/`
- `.env` mit Secrets
- Cache-Dateien
- lokale Credentials

## Baseline

Die Baseline kombiniert einfache Records, Validierung, Filterung und Aggregation. Sie dient als Diagnose, nicht als Prüfung.

```python
records = [
    {"id": 1, "score": 10},
    {"id": 2, "score": "invalid"},
]

valid = []
total = 0

for record in records:
    score = record["score"]
    if isinstance(score, (int, float)):
        valid.append(record)
        total += score
```

## Recall

- Warum verwenden wir ein `venv`?
- Woran erkennst du, welches pip gerade aktiv ist?
- Warum darf `.env` nicht committed werden?
- Was war der Zweck der Baseline?

## Gate

Umgebung selbst erstellen, aktivieren, Script aus Terminal starten, requirements verwalten und den Zweck von Dependency Isolation erklären.
