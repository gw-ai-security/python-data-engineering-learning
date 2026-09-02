#07 LIST OF DICTIONARIES MIT FOR LOOP

customers =[
    {
        "id": 1,
        "name": "Alice",
        "revenue": 1000.0,
        "is_active": True
    },
    {
        "id": 2,
        "name": "Bob",
        "revenue": 2000.0,
        "is_active": False
    },
    {
        "id": 3,
        "name": "Charlie",
        "revenue": 1500.0,
        "is_active": True
    }
]
print("======================================================")

for customer in customers:
        print(f"Customer: {customer['name']} | Revenue: {customer['revenue']}")
print("======================================================")
for customer in customers:
    if customer["is_active"] == True:
        print(f"Customer: {customer['name']} | Revenue: {customer['revenue']}")
print("======================================================")
