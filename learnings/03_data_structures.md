# 03 – Data Structures: List, Tuple, Set, Dictionary

## Wozu dient das?

Daten kommen selten als Einzelwert. Die Wahl der passenden Datenstruktur bestimmt, wie gut Daten gespeichert, gesucht, validiert und transformiert werden können.

## List

Geordnet und veränderbar.

```python
revenues = [100.0, 250.0, 175.0]
revenues.append(300.0)
```

Gut für Sequenzen und `list[dict]`-Records.

## Tuple

Geordnet, aber nicht veränderbar.

```python
coordinate = (48.2, 16.37)
```

## Set

Eindeutige Werte, ideal für Membership und Deduplizierung.

```python
allowed_status = {"active", "inactive"}
if status in allowed_status:
    ...
```

## Dictionary

Key → Value Mapping. Besonders wichtig für JSON.

```python
customer = {
    "id": 1,
    "name": "Alice",
    "country": "AT"
}

print(customer["name"])
```

## Nested Structures

```python
payload = {
    "source": "api",
    "records": [
        {"id": 1, "value": 10},
        {"id": 2, "value": 20}
    ]
}
```

JSON objects map naturally to dictionaries; JSON arrays to lists.

## Data-Engineering-Transfer

- JSON object → `dict`
- JSON array → `list`
- allowed codes → `set`
- table-like records → `list[dict]`
- lookup mapping → `dict`
- duplicate IDs → `set`

## Mutation

Mehrere Variablen können auf dasselbe veränderbare Objekt zeigen. Änderungen können daher unerwartet sichtbar werden. Das wird beim Kopieren von Records wichtig.

## Recall

- List vs. tuple?
- List vs. set?
- Set vs. dict?
- Warum ist `dict` für APIs zentral?
- Was verursacht einen `KeyError`?

## Gate

Für konkrete Datenprobleme die passende Struktur wählen, implementieren und die Entscheidung begründen.
