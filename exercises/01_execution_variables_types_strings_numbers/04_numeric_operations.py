#04 numeric Operations

unit_price = 24.90
quantity = 15
discount_rate = 0.10

#Numeric Operations
gross_value = unit_price * quantity
discount_amount = gross_value * discount_rate
net_value = gross_value - discount_amount

print("===============================================")
print(f"Gross Value: {gross_value}")
print(f"Discount Amount: {discount_amount}")
print(f"Net Value: {net_value}")
print("===============================================")
#Types
print(type(gross_value))
print(type(discount_amount))
print(type(net_value))
print("===============================================")
