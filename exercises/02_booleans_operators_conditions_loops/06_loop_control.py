transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": -50},
    {"id": 3, "amount": 200},
    {"id": 4, "amount": -999},
    {"id": 5, "amount": 300}
]

#Business Rule
#amount < 0
#→ Record überspringen

#amount == -999
#→ Verarbeitung vollständig abbrechen

for transaction in transactions:
    amount = transaction["amount"]

    if amount == -999:
        print(f"Transaction {transaction['id']} processing aborted due to special amount: {amount}")
        break

    if amount < 0:
        print(f"Transaction {transaction['id']} skipped due to negative amount: {amount}")
        continue

    print(f"Processing Transaction {transaction['id']} with amount: {amount}")
