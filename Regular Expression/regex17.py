import re

s = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', s, re.I)

for i in range(len(words) - 1):
    if words[i].lower() == words[i + 1].lower():
        print("Repeated word:", words[i])