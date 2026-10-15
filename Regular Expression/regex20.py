import re

s = input("Enter filenames: ")
print(re.findall(r'\b[\w-]+\.(\w+)\b', s))