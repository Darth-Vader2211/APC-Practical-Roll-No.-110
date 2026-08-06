"""27.	Email Validator 
•	Validate whether a given email address follows a valid format. """
import re

email = input("Enter email: ")

pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")