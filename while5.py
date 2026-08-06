"""Write a PYTHON program to print sum of odd numbers up to n"""
n = int(input("Enter n: "))

sum = 0
for i in range(1, n + 1, 2):
    sum += i

print("Sum =", sum)