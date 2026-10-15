import re

s = input("Enter password: ")

if re.fullmatch(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])\S{8,}', s):
    print("Strong password")
else:
    print("Weak password")