#03 Type Casting

raw_year = "2026"
raw_quantity = "15"
raw_price = "24.90"

#Variables with Type casted Values
year_int = int(raw_year)
quantity_int = int(raw_quantity)
price_float = float(raw_price)
total_value = quantity_int * price_float

print(f"Year: {year_int}")
print(f"Quantity: {quantity_int}")
print(f"Price: {price_float}")
print(f"Total Value: {total_value}")
