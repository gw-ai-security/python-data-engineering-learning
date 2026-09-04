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

## Requirements-Strategie

`requirements.txt` ist aktuell absichtlich ohne Third-Party-Runtime-Abhängigkeiten. Es werden keine Pakete nur für einen künstlichen Setup-Test hinzugefügt. Sobald ein späterer Block die erste echte Library benötigt, wird sie im aktiven `.venv` installiert und reproduzierbar im Requirements-Workflow dokumentiert.

Das bedeutet: Die Umgebung ist praktisch einsatzbereit, der strikte Lernplan-Punkt „Paket installieren / requirements erzeugen“ wird jedoch erst beim ersten realen Dependency-Use-Case vollständig evidenziert.

## Recall

- Warum verwenden wir ein `venv`?
- Woran erkennst du, welches pip gerade aktiv ist?
- Warum darf `.env` nicht committed werden?
- Was war der Zweck der Baseline?
- Warum ist ein absichtlich leeres `requirements.txt` besser als künstliche Dependencies?

## Gate

Umgebung selbst erstellen, aktivieren, Script aus Terminal starten, eine echte Projektdependency im `.venv` installieren und reproduzierbar dokumentieren sowie den Zweck von Dependency Isolation erklären.

**Aktueller Status:** Umgebung und Baseline operational; der reale Dependency-/Requirements-Checkpoint wird beim ersten tatsächlich benötigten Third-Party-Paket abgeschlossen.
