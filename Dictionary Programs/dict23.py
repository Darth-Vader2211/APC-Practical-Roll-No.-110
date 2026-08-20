#23.	Given a list of numbers, create a dictionary containing each unique number and its frequency.

numbers = [4, 2, 8, 2, 4, 9, 4, 1, 8, 2]

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Numbers list:", numbers)
print("Frequency dictionary:", frequency)
