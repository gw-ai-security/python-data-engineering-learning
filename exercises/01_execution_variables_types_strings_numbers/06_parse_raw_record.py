#06 Parse raw record

raw_record = "  1001 | alice smith | austria | 3 | 24.90  "

#customer_id    → 1001        int
#customer_name  → Alice Smith str
#country        → Austria     str
#quantity       → 3           int
#unit_price     → 24.9        float
#total_value    → 74.7        float

splitted_record = raw_record.split("|")

customer_id = int(splitted_record[0].strip())
customer_name = splitted_record[1].strip().title()
country = splitted_record[2].strip().title()
quantity = int(splitted_record[3].strip())
unit_price = float(splitted_record[4].strip())
total_value = round(unit_price * quantity,1)

print(f"Customer ID: {customer_id}")
print(f"Customer: {customer_name}")
print(f"Country: {country}")
print(f"Quantity: {quantity}")
print(f"Unit Price: {unit_price}")
print(f"Total Value: {total_value}")
