# 07 – HTTP and REST API Ingestion

## Wozu dient das?

Viele Quellsysteme stellen Daten über HTTP APIs bereit. Ein Data Engineer muss Requests kontrolliert ausführen, Responses prüfen und Rohdaten reproduzierbar sichern können.

## Mental Model

```text
Client → HTTP Request → Server
Client ← HTTP Response ← Server
```

Ein Endpoint ist eine URL für eine konkrete Ressource oder Operation.

## GET Request

Konzeptionelles Beispiel mit `requests`:

```python
import requests

response = requests.get(
    "https://example.org/api/items",
    timeout=10
)

response.raise_for_status()
payload = response.json()
```

## Wichtige Bestandteile

- URL / Endpoint
- Query Parameters
- Headers
- Status Code
- JSON Body
- Timeout
- Pagination
- Authentication konzeptionell
- Rate Limits
- Retry

## Status Codes

- `2xx` – erfolgreich
- `4xx` – Request / Client Problem
- `5xx` – Server Problem

Nicht blind `.json()` aufrufen, bevor die Response plausibel geprüft wurde.

## Timeout

Ohne Timeout kann ein Request sehr lange hängen. Reliability beginnt mit kontrolliertem Verhalten.

## Pagination

Eine API liefert häufig nicht alle Records auf einmal. Die Pipeline muss wissen, wann die nächste Seite geladen wird und wann Schluss ist.

## Raw Persistence

```text
API → Response prüfen → JSON parsen → Raw Response speichern
```

Raw-Daten helfen bei Debugging, Traceability und erneutem Processing.

## Retry-Risiko

Ein Retry darf nicht unkontrolliert Duplikate erzeugen. Idempotenz wird später vertieft.

## Gate

Ohne Tutorial einen Client bauen, der Request, Statusprüfung, Timeout, JSON-Verarbeitung, Fehlerbehandlung und Raw-Sicherung beherrscht.
