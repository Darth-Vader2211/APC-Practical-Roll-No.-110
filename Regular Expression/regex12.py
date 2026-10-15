import re

s = input("Enter email address: ")

if re.fullmatch(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}', s):
    print("Valid email")
else:
    print("Invalid email")