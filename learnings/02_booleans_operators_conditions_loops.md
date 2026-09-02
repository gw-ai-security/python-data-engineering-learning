# 02 – Booleans, Operators, Conditions, Loops

## Wozu dient das?

Hier bekommt Code Entscheidungslogik. Data Pipelines müssen Records akzeptieren, ablehnen oder unterschiedlich behandeln.

## Booleans und Vergleiche

```python
quantity = 5
is_valid = quantity > 0
```

Vergleichsoperatoren: `==`, `!=`, `>`, `<`, `>=`, `<=`.

Logische Operatoren:

```python
is_valid = quantity > 0 and status == "active"
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

Eine technisch korrekte Bedingung kann fachlich trotzdem falsch sein. Die Business Rule muss zuerst klar sein.

## `for`

Für bekannte Collections:

```python
for record in records:
    print(record)
```

## `while`

Für Wiederholung solange eine Bedingung gilt:

```python
page = 1
while page <= 3:
    print(page)
    page += 1
```

`break` beendet die Schleife, `continue` springt zum nächsten Durchlauf.

## Data-Engineering-Transfer

```python
valid_records = []
rejected_records = []

for record in records:
    if record["quantity"] > 0:
        valid_records.append(record)
    else:
        rejected_records.append(record)
```

Später gehört auch ein `rejection_reason` dazu.

## Typische Fehler

- Off-by-one bei `range`
- falsche Kombination von `and` / `or`
- Endlosschleife bei `while`
- Boundary Values nicht testen

## Recall

- Wann `for`, wann `while`?
- Unterschied `break` vs. `continue`?
- Warum muss eine Business Rule getrennt von ihrer Syntax beurteilt werden?

## Gate

Mindestens fünf Validierungsregeln selbst implementieren und Records nachvollziehbar in valid / rejected aufteilen.
