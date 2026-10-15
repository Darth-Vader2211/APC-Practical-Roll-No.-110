import re

s = input("Enter a paragraph: ")
print(re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', s))