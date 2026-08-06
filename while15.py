"""Write a PYTHON program to print the largest of n numbers"""
n = int(input("Enter the number of elements: "))

largest = float("-inf")

for i in range(n):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print("Largest number =", largest)