#4.	Create a set of numbers and remove a specified number from the set.

numbers = {10, 20, 30, 40, 50}
num_to_remove = int(input("Enter a number to remove: "))

if num_to_remove in numbers:
    numbers.remove(num_to_remove)
    print(f"Number {num_to_remove} removed.")
else:
    print("Number not found in the set.")

print("Updated set:", numbers)
