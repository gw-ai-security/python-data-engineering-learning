#04 - customer Validation Loop

# # List of dictionaries key-value pairs for each customer
customers = [
    {
        "name": "Alice",
        "country": "Austria",
        "age": 25,
        "is_active": True,
        "revenue": 1200,
        "is_blocked": False
    },
    {
        "name": "Bob",
        "country": "Germany",
        "age": 17,
        "is_active": True,
        "revenue": 800,
        "is_blocked": False
    },
    {
        "name": "Charlie",
        "country": "Austria",
        "age": 30,
        "is_active": False,
        "revenue": 1500,
        "is_blocked": False
    },
    {
        "name": "David",
        "country": "Germany",
        "age": 22,
        "is_active": True,
        "revenue": 1000,
        "is_blocked": False
    },
    {
        "name": "Eve",
        "country": "France",
        "age": 28,
        "is_active": True,
        "revenue": 1200,
        "is_blocked": False
    }
]

#Initialize lists to store eligible and rejected customers
eligible_customers = []
rejected_customers = []

#Loop through the list of customers and check eligibility
for customer in customers:
    country_is_eligible = customer["country"] in ("Austria", "Germany")
    age_is_eligible = customer["age"] >= 18
    customer_is_active = customer["is_active"]
    revenue_is_eligible = customer["revenue"] >= 1000
    customer_is_not_blocked = not customer["is_blocked"]

    #Check if the customer meets all eligibility criteria
    customer_is_eligible = (
        country_is_eligible
        and age_is_eligible
        and customer_is_active
        and revenue_is_eligible
        and customer_is_not_blocked
    )
    #Add the customer to the appropriate list based on eligibility
    if customer_is_eligible:
        eligible_customers.append(customer)
    else:
        rejected_customers.append(customer)

print("--------------------------------------------------")
#Print the results
print("Eligible Customers:")
print("--------------------------------------------------")
for customer in eligible_customers:
    print(f"- {customer['name']}")

print("--------------------------------------------------")

print("Rejected Customers:")
print("--------------------------------------------------")
for customer in rejected_customers:
    print(f"- {customer['name']}")
print("--------------------------------------------------")
