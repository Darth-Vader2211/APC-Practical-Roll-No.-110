#17.	Find the largest and smallest number in a tuple without using max() and min().

numbers = (45, 12, 89, 34, 67, 23, 90, 11)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Numbers tuple:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
