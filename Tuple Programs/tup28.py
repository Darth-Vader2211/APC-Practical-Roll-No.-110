#28.	Count the frequency of each element in a tuple.

data = (1, 2, 2, 3, 4, 4, 4, 5, 1, 2)

frequency = {}
for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Tuple:", data)
print("Element frequencies:")
for elem, count in frequency.items():
    print(f"{elem}: {count}")
