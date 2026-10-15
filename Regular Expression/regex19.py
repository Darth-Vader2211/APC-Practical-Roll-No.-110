import re

s = input("Enter vehicle number: ")

if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}', s):
    print("Valid format")
else:
    print("Invalid format")