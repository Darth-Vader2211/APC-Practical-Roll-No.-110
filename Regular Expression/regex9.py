import re

s = input("Enter a string: ")
s = re.sub(r'[^a-zA-Z0-9 ]', '', s)
print(s)