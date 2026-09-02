#08 ISINSTANCE Checks if an object is an instance of a class or a subclass thereof.

customers = [
    {"id": 1, "name": "Alice", "revenue": 1000.0},
    {"id": 2, "name": "Bob", "revenue": "invalid"},
    {"id": 3, "name": "Charlie", "revenue": 1500},
    {"id": 4, "name": "Diana", "revenue": None}
]

for customer in customers:
    revenue = customer["revenue"]
    if isinstance(revenue, (int, float)):
        print(f"Valid revenue: {customer['name']} | Revenue: ${revenue}")
    else:
        print(f"Invalid revenue: {customer['name']}")
