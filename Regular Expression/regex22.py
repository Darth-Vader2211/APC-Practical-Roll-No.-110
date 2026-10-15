import re

s = input("Enter invoice text: ")

print("Invoice numbers:", re.findall(r'Invoice\s*No\.?\s*:\s*(\w+)', s, re.I))
print("Dates:", re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s))
print("Amounts:", re.findall(r'₹\s*[\d,]+(?:\.\d{2})?', s))