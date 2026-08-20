'''15.	Duplicate Characters 
a.	Print all duplicate characters in a string.'''
s = input("Enter a string: ")

print("Duplicate characters:")
for ch in set(s):
    if s.count(ch) > 1:
        print(ch)