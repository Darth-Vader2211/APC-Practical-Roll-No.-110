#33.	Take a string, use a dictionary to find the first character that occurs only once.

text = "swiss"

freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

first_unique = None
for char in text:
    if freq[char] == 1:
        first_unique = char
        break

print("String:", text)
if first_unique:
    print(f"First character that occurs only once: '{first_unique}'")
else:
    print("No non-repeating character found.")
