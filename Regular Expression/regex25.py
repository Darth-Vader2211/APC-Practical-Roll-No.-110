import re

s = input("Enter student details: ")

result = re.search(
    r'Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)',
    s
)

if result:
    print("Name:", result.group(1))
    print("Roll Number:", result.group(2))
    print("Marks:", result.group(3))
else:
    print("Invalid format")