#34.	Take a string, use a dictionary to find the first character that occurs more than once.

text = "swiss"

counts = {}
first_repeat = None

for char in text:
    if char in counts:
        first_repeat = char
        break
    counts[char] = 1

print("String:", text)
if first_repeat:
    print(f"First character that occurs more than once: '{first_repeat}'")
else:
    print("No repeating character found.")
