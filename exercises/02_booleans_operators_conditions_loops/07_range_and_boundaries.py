# 07 Range and Boundaries

print("======================================================")

# Print exactly five numbers from 1 to 5.
for number in range(1, 6):
    print(number)

print("======================================================")

# Simulate API pages 1 to 3.
for page in range(1, 4):
    print(f"Processing page {page}")

print("======================================================")

# The stop value of range() is exclusive, so 5 is not printed here.
for number in range(1, 5):
    print(number)

print("======================================================")

max_page = 5

# +1 converts the inclusive business boundary into range()'s exclusive stop value.
for page in range(1, max_page + 1):
    print(f"Page {page}")

print("======================================================")
