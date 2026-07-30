"""Remove Spaces 
•	Remove all spaces from the input string. 
"""
s1 = input("Enter a String:")
for i in s1:
    if i == " ":
        s1 = s1.replace(" ", "")
print("Updated String is: ",s1)