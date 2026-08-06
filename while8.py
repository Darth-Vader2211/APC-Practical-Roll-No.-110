"""Write a PYTHON program to print Fibonacci series up to n"""
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c