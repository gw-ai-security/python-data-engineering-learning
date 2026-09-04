# 10 Independent Gate

transactions = [
    {
        "id": "TX-001",
        "country": "Austria",
        "amount": 1200,
        "is_active": True,
        "is_blocked": False,
    },
    {
        "id": "TX-002",
        "country": "Germany",
        "amount": -50,
        "is_active": True,
        "is_blocked": False,
    },
    {
        "id": "TX-003",
        "country": "France",
        "amount": 800,
        "is_active": True,
        "is_blocked": False,
    },
    {
        "id": "TX-004",
        "country": "Austria",
        "amount": 1500,
        "is_active": False,
        "is_blocked": False,
    },
    {
        "id": "TX-005",
        "country": "Germany",
        "amount": 2000,
        "is_active": True,
        "is_blocked": True,
    },
]

# Business rules:
# - id starts with "TX-"
# - country is Austria or Germany
# - amount > 0
# - customer is active
# - customer is not blocked

accepted_transactions = []
rejected_transactions = []

for transaction in transactions:
    rejection_reasons = []

    id_is_valid = transaction["id"].startswith("TX-")
    country_is_valid = transaction["country"] in ("Austria", "Germany")
    amount_is_valid = transaction["amount"] > 0
    customer_is_active = transaction["is_active"]
    customer_is_not_blocked = not transaction["is_blocked"]

    if not id_is_valid:
        rejection_reasons.append("ID must start with TX-")
    if not country_is_valid:
        rejection_reasons.append("country must be Austria or Germany")
    if not amount_is_valid:
        rejection_reasons.append("amount must be greater than 0")
    if not customer_is_active:
        rejection_reasons.append("customer is not active")
    if not customer_is_not_blocked:
        rejection_reasons.append("customer is blocked")

    if rejection_reasons:
        rejected_transactions.append(
            {"id": transaction["id"], "reasons": rejection_reasons}
        )
    else:
        accepted_transactions.append(transaction)

print("===================================================")
print(f"Accepted: {len(accepted_transactions)}")
print(f"Rejected: {len(rejected_transactions)}")
print("===================================================")

for accepted_transaction in accepted_transactions:
    print(f"{accepted_transaction['id']} ACCEPTED")

print("===================================================")

for rejected_transaction in rejected_transactions:
    print(
        f"{rejected_transaction['id']}: REJECTED - "
        f"{rejected_transaction['reasons']}"
    )

print("===================================================")
