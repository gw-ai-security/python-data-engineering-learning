# 02 – Booleans, Operators, Conditions, Loops

## Wozu dient das?

Hier bekommt Code Entscheidungslogik. Data Pipelines müssen Records akzeptieren, ablehnen, klassifizieren, überspringen oder die Verarbeitung kontrolliert stoppen.

## Booleans und Vergleiche

```python
quantity = 5
is_valid = quantity > 0
```

Vergleichsoperatoren:

```text
==  !=  >  <  >=  <=
```

Jeder Vergleich erzeugt einen Boolean.

```python
score = 80
print(score >= 50)  # True
```

Wichtig:

```python
country = "Austria"   # assignment
country == "Austria"  # comparison
```

## Logische Operatoren

```python
is_valid = quantity > 0 and status == "active"
```

Mental Model:

```text
and → alle Bedingungen müssen True sein
or  → mindestens eine Bedingung muss True sein
not → Boolean umkehren
```

Beispiel:

```python
country_is_eligible = country in ("Austria", "Germany")
customer_is_not_blocked = not is_blocked
```

## Conditions

```python
if quantity > 0:
    print("valid")
elif quantity == 0:
    print("zero")
else:
    print("invalid")
```

Bei `if / elif / else` wird von oben nach unten geprüft. Der erste passende Zweig gewinnt.

Deshalb müssen überlappende Schwellen bewusst sortiert werden:

```python
if value >= 1000:
    classification = "high"
elif value >= 500:
    classification = "medium"
else:
    classification = "low"
```

Eine technisch korrekte Bedingung kann fachlich trotzdem falsch sein. Die Business Rule muss zuerst klar sein.

## Mehrere unabhängige `if`-Regeln

Wenn mehrere Fehler gleichzeitig erkannt werden sollen, ist `elif` oft falsch:

```python
reasons = []

if age < 18:
    reasons.append("underage")

if revenue < 1000:
    reasons.append("revenue_below_threshold")
```

Ein Record kann damit mehrere Rejection Reasons erhalten.

## `for`

Für bekannte Collections:

```python
for record in records:
    print(record)
```

Ein typisches Data-Engineering-Muster:

```python
valid_records = []
rejected_records = []

for record in records:
    if record["quantity"] > 0:
        valid_records.append(record)
    else:
        rejected_records.append(record)
```

## Strukturierte Rejection Reasons

Ablehnungsgründe sollten nicht als schwer auswertbare Freitextstrings gespeichert werden, wenn sie später maschinell gebraucht werden.

```python
rejected_records.append({
    "record": record,
    "reasons": ["underage", "revenue_below_threshold"]
})
```

Mental Model:

```text
record
+ validation result
+ rejection reasons
```

Das ist bereits eine einfache Vorstufe von Data-Quality-/Reject-Table-Logik.

## `continue` und `break`

```python
for transaction in transactions:
    if transaction["amount"] == -999:
        break

    if transaction["amount"] < 0:
        continue

    print(transaction)
```

- `continue` beendet nur den aktuellen Durchlauf und geht zum nächsten Element.
- `break` beendet die gesamte Schleife.

Die Reihenfolge kann fachlich entscheidend sein. Wenn `-999` ebenfalls `< 0` ist, muss der spezifische Stop-Fall vor der allgemeinen Negativ-Regel geprüft werden.

## `while`

Für Wiederholung solange eine Bedingung gilt:

```python
page = 1
while page <= 3:
    print(page)
    page += 1
```

Mental Model:

```text
INITIAL STATE
→ CHECK CONDITION
→ DO WORK
→ CHANGE STATE
→ CHECK AGAIN
```

`while` ist besonders relevant, wenn nicht eine bekannte Collection durchlaufen wird, sondern eine Abbruchbedingung den Ablauf steuert, etwa Pagination oder Retry-Logik.

Risiko: Wenn die Bedingung nie `False` wird, entsteht eine Endlosschleife.

## `range`

`range` erzeugt eine Folge von Ganzzahlen für Schleifen:

```python
for i in range(3):
    print(i)
```

Ausgabe:

```text
0
1
2
```

Das Stop-Ende ist exklusiv. Für eine inklusive fachliche Obergrenze wird deshalb häufig `max_value + 1` benötigt:

```python
for page in range(1, max_page + 1):
    print(page)
```

Genau daraus entstehen typische Off-by-one-Fehler.

## Boundary Values

Regeln sollten an den Grenzen getestet werden.

Wenn gilt:

```python
age >= 18
```

sind mindestens diese Fälle interessant:

```text
17 → False
18 → True
19 → True
```

Für `revenue >= 1000` entsprechend `999`, `1000`, `1001`.

Bei Schleifen gilt dieselbe Denkweise: Prüfe explizit den ersten und letzten gewünschten Wert sowie den ersten Wert außerhalb des gültigen Bereichs.

## Debugging von Schleifenbedingungen

Das verwendete Protokoll lautet:

```text
OBSERVE
→ HYPOTHESIZE
→ ISOLATE
→ TEST
→ FIX
→ VERIFY
→ PREVENT
```

Wichtig: `OBSERVE` beschreibt zunächst nur das tatsächliche Verhalten. Die vermutete Ursache gehört erst in `HYPOTHESIZE`.

Zwei typische Fehlerbilder dieses Blocks:

- `page < max_page` statt `page <= max_page` → obere Boundary wird nicht verarbeitet;
- fehlendes `attempt += 1` in einer `while`-Schleife → Zustand verändert sich nicht, Schleife terminiert nicht.

## Data-Engineering-Transfer

- Validierungsregeln als Booleans modellieren
- mehrere Business Rules kombinieren
- Records accepted/rejected aufteilen
- strukturierte Rejection Reasons erzeugen
- Schwellenwerte korrekt klassifizieren
- ungültige Rows überspringen
- kritische Stop-Bedingungen erkennen
- Pagination / kontrollierte Wiederholung mit `while`
- Retry-Zähler sicher terminieren
- `range`-Grenzen für Pages, Batches oder Partitionen korrekt setzen
- Boundary Values und Off-by-one-Fälle prüfen

## Praktische Evidenz im Repository

Implementiert:

1. `01_transaction_validation.py`
2. `02_transaction_classification.py`
3. `03_customer_eligibility.py`
4. `04_customer_validation_loop.py`
5. `05_rejection_reasons.py`
6. `06_loop_control.py`
7. `07_range_and_boundaries.py`
8. `08_while_loop.py`
9. `09_debug_loop_conditions.py`
10. `10_independent_gate.py`

Der Independent Gate kombiniert fünf Business Rules, Record-by-Record-Verarbeitung, accepted/rejected Collections, strukturierte Rejection Reasons und Count-Ausgaben ohne Funktionsabstraktion oder Schritt-für-Schritt-Lösungsvorlage.

## Typische Fehler

- `=` mit `==` verwechseln
- Boolean durch eine Zuweisung versehentlich überschreiben
- falsche Kombination von `and` / `or`
- überlappende `if / elif`-Regeln in falscher Reihenfolge
- `elif` verwenden, obwohl mehrere Fehler gleichzeitig gesammelt werden sollen
- globale Rejection-Reason-Strings bauen und später per Textsuche zu Records zurückzuordnen
- Spezialfall nach einer allgemeineren Bedingung prüfen
- Off-by-one bei `range`
- Endlosschleife bei `while`
- Boundary Values nicht testen

## Recall

- Wann `for`, wann `while`?
- Unterschied `break` vs. `continue`?
- Warum kann die Reihenfolge von Bedingungen das Ergebnis verändern?
- Wann mehrere `if` statt `if / elif`?
- Warum Rejection Reasons strukturiert speichern?
- Warum muss eine Business Rule getrennt von ihrer Syntax beurteilt werden?
- Wie teste ich Boundary Values?
- Warum ist das Stop-Ende von `range` eine typische Fehlerquelle?
- Welche State-Änderung sorgt dafür, dass eine `while`-Schleife terminiert?

## Gate

Mindestens fünf Validierungsregeln ohne Schritt-für-Schritt-Vorlage implementieren, Records nachvollziehbar in valid/rejected aufteilen, Rejection Reasons erzeugen und typische Boundary-/Loop-Fehler selbst debuggen.

**Status: Gate passed on 2026-09-04.**
