"""6.	Replace Characters 
•	Replace all occurrences of a given character with another character
"""
s1 = input("Enter a String: ")
old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")
for i in s1:
    if i == old_char:
        s1 = s1.replace(old_char, new_char)
print("Updated String: ", s1)