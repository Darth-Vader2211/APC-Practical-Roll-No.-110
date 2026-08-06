"""Write a PYTHON program to print smallest of n numbers"""
n = int(input("Enter the number of elements: "))

smallest = float("inf")

for i in range(n):
    num = int(input("Enter a number: "))
    if num < smallest:
        smallest = num

print("Smallest number =", smallest)