import re

s = input("Enter text: ")
print("Spaces:", len(re.findall(r' ', s)))
print("Tabs:", len(re.findall(r'\t', s)))
print("Newlines:", len(re.findall(r'\n', s)))