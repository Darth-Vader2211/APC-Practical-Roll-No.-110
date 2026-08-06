"""21.Password Validator
•	Validate a password based on these conditions: 
o	Minimum 8 characters 
o	At least one uppercase letter 
o	One lowercase letter 
o	One digit 
o	One special character"""
import re

password = input("Enter password: ")

if (len(password) >= 8 and
    re.search("[A-Z]", password) and
    re.search("[a-z]", password) and
    re.search("[0-9]", password) and
    re.search("[@#$%^&*!]", password)):
    print("Valid Password")
else:
    print("Invalid Password")