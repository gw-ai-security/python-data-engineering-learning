customers = [
    {'id': 1, 'name': 'Alice', 'score': 10},
    {'id': 2, 'name': 'Bob', 'score': 15},
    {'id': 3, 'name': 'Charlie', 'score': 12},
    {'id': 4, 'name': 'David', 'score': 'eight'},
    {'id': 5, 'name': 'Eve', 'score': 20}
]

valid_records = []
sum_valid_scores = 0

for customer in customers:
    score = customer['score']

    if isinstance(score, (int, float)):
        valid_records.append(customer)
        sum_valid_scores += score

print("======================================================")

for customer in valid_records:
    print(f"Valid Record: {customer}")

print("======================================================")
print(f"Sum of Valid Scores: {sum_valid_scores}")
print("======================================================")
