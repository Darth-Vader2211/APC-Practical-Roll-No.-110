#19.	Store 15 integers in a tuple and count:
#	•	Even numbers 
#	•	Odd numbers

numbers = (12, 7, 19, 24, 30, 15, 8, 41, 52, 63, 74, 85, 96, 11, 20)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers tuple:", numbers)
print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
