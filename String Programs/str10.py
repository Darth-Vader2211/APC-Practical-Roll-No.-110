"""10.	ASCII Values 
•	Display each character of a string along with its ASCII value.
"""
s1 = input("Enter a String: ")
for ch in s1:
    print(ord(ch), end=' ')