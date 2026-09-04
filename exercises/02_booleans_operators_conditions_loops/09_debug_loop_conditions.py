# 09 Debug Loop Conditions

print("===========================================================")

page = 1
max_page = 3

# OBSERVE:
# Expected pages 1, 2 and 3. A condition using page < max_page would only process 1 and 2.
#
# HYPOTHESIZE:
# The upper boundary is excluded because the loop condition uses < instead of <=.
#
# ISOLATE:
# The relevant expression is the while condition.
#
# TEST:
# Change the condition to page <= max_page and run the script again.
#
# FIX:
# Use <= so the maximum page is included.
#
# VERIFY:
# Pages 1, 2 and 3 are processed exactly once.
#
# PREVENT:
# Test lower and upper boundary values explicitly when writing loop conditions.

while page <= max_page:
    print(f"Processing page {page}")
    page += 1

print("===========================================================")

# Example 2: without incrementing attempt, the condition would remain True forever.
attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print(f"Attempt {attempt}")
    attempt += 1

print("===========================================================")
