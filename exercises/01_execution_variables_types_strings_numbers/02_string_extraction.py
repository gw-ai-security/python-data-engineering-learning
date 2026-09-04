#02 String Extraction

product_code = "AT-VIE-2026-001"

country_code = product_code[0:2]
city_code = product_code[3:6]
year = product_code[7:11]
sequence = product_code[-3:]


print(f"Country: {country_code}")
print(f"City: {city_code}")
print(f"Year: {year}")
print(f"Sequence: {sequence}")
