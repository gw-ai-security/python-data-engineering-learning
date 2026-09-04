#07 String Validation

raw_customer_id = "1001"
raw_product_code = "AT-VIE-2026-001"
raw_file_name = "customers.csv"
raw_country = "Austria"

customer_id_is_numeric = raw_customer_id.isdigit()
product_code_is_austrian = raw_product_code.startswith("AT-")
file_is_csv = raw_file_name.endswith(".csv")
country_is_letters_only = raw_country.isalpha()

print(f"Customer ID numeric: {customer_id_is_numeric}")
print(f"Product code starts with AT-: {product_code_is_austrian}")
print(f"File is CSV: {file_is_csv}")
print(f"Country contains only letters: {country_is_letters_only}")
