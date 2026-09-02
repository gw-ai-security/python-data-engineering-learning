revenues = [1000.0, 2000.0, -500.0, 3000.0, 0.0]
valid_revenues = []
total_valid_revenue = 0

for revenue in revenues:
    if revenue > 0:
        valid_revenues.append(revenue)
        total_valid_revenue += revenue

print(valid_revenues)
print(f"Total Valid Revenue: ${total_valid_revenue}")
