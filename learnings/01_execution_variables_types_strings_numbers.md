# 01 – Python Execution, Variables, Types, Strings, Numbers

## Wozu dient das?

Data Engineering bedeutet ständig Werte zu lesen, zu prüfen und zu standardisieren. Dafür musst du verstehen, welchen Wert eine Variable hält, welchen Datentyp dieser Wert hat und welche Annahmen eine Transformation macht.

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

Data-Engineering-Regel: Nicht alles, was nur aus Ziffern besteht, ist fachlich eine Zahl. Eine ID wie `"001"` kann absichtlich ein String bleiben, weil Arithmetik darauf keinen Business-Sinn hat und führende Nullen relevant sein können.

## Strings standardisieren

```python
country = "  austria "
clean_country = country.strip().title()
```

Typische Werkzeuge:

- `.strip()` – Rand-Whitespace entfernen
- `.lower()` / `.upper()` / `.title()` – Case normalisieren
- `.replace()` – Text ersetzen
- slicing – Ausschnitte lesen
- `.split()` – einen strukturierten String an einem Delimiter zerlegen
- f-Strings – Werte lesbar formatieren

```python
code = "AT-VIE-2026-001"
country_code = code[:2]
parts = code.split("-")
print(parts)  # ['AT', 'VIE', '2026', '001']
```

### Annahmen bei Normalisierung

Eine String-Methode ist nicht automatisch fachlich korrekt.

```python
name = "o'neill"
print(name.title())
```

`.title()` ist für einfache Lernbeispiele nützlich, aber keine universell sichere Personennamen-Normalisierung. Transformationen müssen zur Semantik des Feldes passen.

## String-Validierung

Transformation verändert einen Wert; Validierung prüft eine Eigenschaft.

```python
raw_customer_id = "1001"
product_code = "AT-VIE-2026-001"
file_name = "customers.csv"

print(raw_customer_id.isdigit())
print(product_code.startswith("AT-"))
print(file_name.endswith(".csv"))
```

Weitere einfache Checks:

```python
"Austria".isalpha()   # True
"New York".isalpha() # False because of the space
```

Solche Checks sind bewusst einfach. Später werden Validierungsregeln strukturierter und robuster.

## Numbers

```python
quantity = 4
unit_price = 12.5
revenue = quantity * unit_price
```

Wichtig: `"100"` ist Text, `100` eine Zahl.

Wenn bei einer arithmetischen Operation ein `float` beteiligt ist, ist das Ergebnis typischerweise ebenfalls ein `float`:

```python
24.90 * 15  # 373.5, type float
```

## Float-Präzision

Binäre Gleitkommazahlen können viele Dezimalbrüche nicht exakt darstellen:

```python
print(0.1 + 0.2)
# 0.30000000000000004
```

Das ist besonders bei Finanzarithmetik relevant. Für diese Lernphase reicht die Erkenntnis; exakte Geldarithmetik wird nicht vorgezogen, bevor sie praktisch benötigt wird.

## Raw → Clean denken

Rohwerte sollten nicht ohne Grund überschrieben werden:

```python
raw_country = "  aUSTRIA "
clean_country = raw_country.strip().title()
```

Mental Model:

```text
RAW VALUE
→ CLEAN / STANDARDIZED VALUE
→ VALIDATED / TYPED VALUE
```

Das ist die kleine lokale Version des späteren Pipeline-Denkens Raw/Bronze → Clean/Silver → Business-ready.

## Data-Engineering-Transfer

- Produktcodes trimmen und zerlegen
- Ländernamen standardisieren
- numerische Strings casten
- identifier vs. measure unterscheiden
- zusammengesetzte IDs lesen
- einfache String-Validierung
- Rohdatensatz an Delimitern parsen
- Typen nach einer Transformation explizit prüfen

## Praktische Evidenz im Repository

Der aktuelle Übungsblock enthält:

1. String normalization
2. String extraction / slicing
3. Type casting
4. Numeric operations
5. Float precision
6. Raw-record parsing
7. String validation

Siehe `exercises/01_execution_variables_types_strings_numbers/`.

## Typische Fehler

- Zahlen als Strings weiterverarbeiten
- blindes Casting ohne Validierung
- Identifier unnötig numerisch machen
- Originalwerte überschreiben, obwohl Raw-Daten erhalten bleiben sollten
- `.title()` oder andere Case-Regeln ohne fachliche Prüfung verwenden
- `float` als exakt dezimale Geldarithmetik missverstehen
- `.startswith("AT")` verwenden, obwohl eigentlich das strengere Präfix `"AT-"` gemeint ist

## Recall

- Unterschied zwischen Variable, Wert und Typ?
- Warum ist `"100" != 100`?
- Wann kann Casting fehlschlagen?
- Warum kann `"001"` als String sinnvoller sein als `1`?
- Welche String-Transformation verändert die fachliche Bedeutung?
- Transformation vs. Validation?
- Warum kann `0.1 + 0.2` überraschend aussehen?

## Gate

Eine kleine Menge roher Textfelder ohne Schritt-für-Schritt-Vorlage standardisieren, typisieren und validieren und jeden Transformationsschritt samt Annahmen erklären.

**Aktueller Status:** Guided practice complete; unabhängiger Gate-Nachweis noch nicht dokumentiert.
