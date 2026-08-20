"""2.	Character Count 
•	Count the number of vowels, consonants, digits, spaces, and special characters in a given string. """

s1 = input("Enter a String: ")
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
v_count = 0
c_count = 0
d_count = 0
s_count = 0
sp_count = 0

for i in s1:
    if i in vow:
        v_count += 1
    elif i.isalpha():
        c_count += 1
    elif i.isdigit():
        d_count += 1
    elif i.isspace():
        s_count += 1
    else:
        sp_count += 1
print("Vowels: ", v_count)
print("Consonants: ", c_count)
print("Digits: ", d_count)
print("Spaces: ", s_count)
print("Special Characters: ", sp_count)