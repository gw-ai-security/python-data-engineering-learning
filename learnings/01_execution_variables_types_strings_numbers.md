# 01 – Python Execution, Variables, Types, Strings, Numbers

## Wozu dient das?

Data Engineering bedeutet ständig Werte zu lesen, zu prüfen und zu standardisieren. Dafür musst du verstehen, welchen Wert eine Variable hält und welchen Typ dieser Wert hat.

## Variablen und Typen

```python
name = "Alice"       # str
quantity = 3         # int
price = 19.95        # float
is_active = True     # bool
missing = None       # NoneType
```

Python ist dynamisch typisiert: Der Typ gehört zum Wert und wird zur Laufzeit bestimmt.

```python
print(type(price))
```

## Casting

```python
raw_quantity = "42"
quantity = int(raw_quantity)
```

Casting ist riskant, wenn die Quelle nicht garantiert sauber ist:

```python
int("forty-two")  # ValueError
```

## Strings standardisieren

```python
country = "  austria "
clean_country = country.strip().title()
```

Typische Werkzeuge:

- `.strip()` – Rand-Whitespace entfernen
- `.lower()` / `.upper()` – Case normalisieren
- `.replace()` – Text ersetzen
- slicing – Ausschnitte lesen
- f-Strings – Werte lesbar formatieren

```python
code = "AT-2026-001"
country_code = code[:2]
print(f"Country: {country_code}")
```

## Numbers

```python
quantity = 4
unit_price = 12.5
revenue = quantity * unit_price
```

Wichtig: `"100"` ist Text, `100` eine Zahl.

## Data-Engineering-Transfer

- Produktcodes trimmen
- Ländernamen standardisieren
- numerische Strings casten
- zusammengesetzte IDs erzeugen
- leere Strings von `None` unterscheiden

## Typische Fehler

- Zahlen als Strings weiterverarbeiten
- Blindes Casting ohne Validierung
- Originalwerte überschreiben, obwohl Raw-Daten erhalten bleiben sollten

## Recall

- Unterschied zwischen Variable, Wert und Typ?
- Warum ist `"100" != 100`?
- Wann kann Casting fehlschlagen?
- Welche String-Transformation verändert die fachliche Bedeutung?

## Gate

Eine Liste roher Textfelder ohne Vorlage standardisieren und jeden Transformationsschritt erklären.
