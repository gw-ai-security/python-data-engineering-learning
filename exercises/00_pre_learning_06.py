##06A DICTIONARIES

customer = {
        "id": 1,
        "name": "Alice",
        "revenue": 1000.0,
        "is_active": True
         }



print(f"Customer ID: {customer['id']}")
print(f"Customer Name: {customer['name']}")
print(f"Customer Revenue: ${customer['revenue']}")
print(f"Customer Active Status: {customer['is_active']}")


#06B LIST OF DICTIONARIES

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
print(f"Customer 2: {customers[1]['name']}")
