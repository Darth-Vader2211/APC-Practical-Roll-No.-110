"""24.	Most Frequent Character 
•	Find the character with the highest frequency."""
s = input("Enter string: ")

max_char = ""
max_count = 0

for ch in set(s):
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Most Frequent:", max_char)