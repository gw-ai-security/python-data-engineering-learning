#01 String Normalization

# RAW Input
customer_name = "   aLiCe SMITH   "
country = "  aUSTRIA "
product_code = "  abC-123  "

# Copy of RAW Data for Transformation
clean_customer_name = customer_name.strip().title()
clean_country = country.strip().title()
clean_product_code = product_code.strip().upper()

# Output to test Transformation
print(f"Customer: {clean_customer_name}")
print(f"Country: {clean_country}")
print(f"Product Code: {clean_product_code}")
