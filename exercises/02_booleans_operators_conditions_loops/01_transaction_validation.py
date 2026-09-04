# 01 Transaction Validation

customer_id = 1001
country = "Austria"
quantity = 0
unit_price = 24.90
is_active = True

#customer_id > 0
#quantity > 0
#unit_price > 0
#is_active == True

## Validity Check for every variable
customer_id_is_valid = customer_id > 0
quantity_is_valid = quantity > 0
price_is_valid = unit_price > 0
customer_is_active = is_active

# And logic combination
transaction_is_valid = (customer_id_is_valid
                        and quantity_is_valid
                        and price_is_valid
                        and customer_is_active)

print(f"Customer ID valid: {customer_id_is_valid}")
print(f"Quantity valid:  {quantity_is_valid}")
print(f"Price valid: {price_is_valid}")
print(f"Customer active: {customer_is_active}")
print("--------------------------------------------------")

if transaction_is_valid:
    print("Transaction is valid")
else:
    print("Transaction is invalid")
