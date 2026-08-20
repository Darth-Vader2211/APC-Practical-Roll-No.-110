#14.	Accept a string from the user and create a dictionary containing each character and its frequency.

cars = input("Enter a string: ")
frequency = {}
for char in cars:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)