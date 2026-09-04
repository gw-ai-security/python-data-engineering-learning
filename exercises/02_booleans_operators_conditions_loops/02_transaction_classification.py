#02 Transaction calissification

transaction_value = 200

#Business Rule

#transaction_value >= 1000  → "High Value"
#transaction_value >= 500   → "Medium Value"
#sonst                      → "Low Value"

#The order of the checks is important to check the correct span of the value
if transaction_value >= 1000:
    print("High Value")
elif transaction_value >= 500:
    print("Medium Value")
else:
    print("Low Value")
