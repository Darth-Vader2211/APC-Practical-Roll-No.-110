"""5.	Uppercase and Lowercase Count 
•	Count the number of uppercase and lowercase letters in a string
"""
s1 = input("Enter a String: ")
up_count = 0
lw_count = 0
for i in s1:
    if i.isupper():
        up_count +=1
    elif i.islower():
        lw_count +=1
print("Uppercase Letters: ", up_count)
print("Lowercase Letters: ", lw_count)
