#05 - Rejection Reason

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

for customer in customers:
    rejection_reasons = []

    country_is_eligible = customer["country"] in ("Austria", "Germany")
    age_is_eligible = customer["age"] >= 18
    customer_is_active = customer["is_active"]
    revenue_is_eligible = customer["revenue"] >= 1000
    customer_is_not_blocked = not customer["is_blocked"]

    if not country_is_eligible:
        rejection_reasons.append("invalid_country")

    if not age_is_eligible:
        rejection_reasons.append("underage")

    if not customer_is_active:
        rejection_reasons.append("inactive_customer")

    if not revenue_is_eligible:
        rejection_reasons.append("revenue_below_threshold")

    if not customer_is_not_blocked:
        rejection_reasons.append("blocked_customer")

    if rejection_reasons:
        rejected_customers.append({
            "customer": customer,
            "reasons": rejection_reasons
        })
    else:
        eligible_customers.append(customer)

print("--------------------------------------------------")
print("Eligible Customers:")
print("--------------------------------------------------")

for customer in eligible_customers:
    print(f"- {customer['name']}")

print("--------------------------------------------------")
print("Rejected Customers:")
print("--------------------------------------------------")

for rejected_record in rejected_customers:
    print(f"- {rejected_record['customer']['name']}")

    for reason in rejected_record["reasons"]:
        print(f"  Reason: {reason}")

print("--------------------------------------------------")
