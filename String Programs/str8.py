"""8.	Frequency of a Character 
•	Find the number of times a specified character appears in a string. 
"""
s1 = input("Enter a String :")
c = 0
ch = input("Enter a character to find its frequency :")
for i in s1:
    if i == ch:
        c += 1
print("Frequency of character '", ch, "' is : ", c)