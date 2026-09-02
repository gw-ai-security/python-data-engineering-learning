revenues = [1000.0, 2000.0, -500.0, 3000.0, 0.0]

for revenue in revenues:
    if revenue > 0:
        print(f"Valid revenue: ${revenue}")
    else:
        print(f"Invalid revenue: ${revenue}")
