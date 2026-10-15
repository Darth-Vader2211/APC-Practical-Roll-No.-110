import re

s = input("Enter a string: ")
vowels = re.findall(r'[aeiou]', s, re.I)
print("Vowel count:", len(vowels))