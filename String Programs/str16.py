"""16.	Character Frequency 
a.	Display the frequency of every character in a string."""
s = input("Enter a string: ")

for ch in set(s):
    print(ch, ":", s.count(ch))