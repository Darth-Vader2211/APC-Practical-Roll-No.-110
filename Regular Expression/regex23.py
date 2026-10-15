import re

s = input("Enter Python source code: ")
print(re.findall(r'#.*', s))