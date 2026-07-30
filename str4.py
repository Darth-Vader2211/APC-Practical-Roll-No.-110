"""Palindrome Check 
•	Check whether the entered string is a palindrome. 
"""
s1 = input("Enter a String: ")
rev = s1[::-1]
if s1 == rev:
    print("Entered String is a Palindrome")
else:
    print("Entered String is not a Palindrome")