#03 Customer Eligibility

country = "Germany"
age = 42
is_active = True
revenue = 1200
is_blocked = False

#Eligible IF

#country ist Austria ODER Germany
#UND
#age >= 18
#UND
#is_active ist True
#UND
#revenue >= 1000

# Check variable Values seperate

country_is_eligible = country in ("Austria", "Germany")
age_is_eligible = age >= 18
customer_is_active = is_active
revenue_is_eligible = revenue >= 1000
customer_is_not_blocked = not is_blocked

customer_is_eligible = (
    country_is_eligible
    and age_is_eligible
    and customer_is_active
    and revenue_is_eligible
    and customer_is_not_blocked
)

if customer_is_eligible:
    print("Eligible")
else:
    print("Not Eligible")

