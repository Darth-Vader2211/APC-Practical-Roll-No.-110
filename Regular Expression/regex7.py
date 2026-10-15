import re

s = input("Enter a sentence: ")
print(re.findall(r'\b\w{5}\b', s))