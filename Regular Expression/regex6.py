import re

s = input("Enter a string: ")
s = re.sub(r' +', ' ', s)
print(s)