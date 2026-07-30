#Write a short PYTHON program to check weather the square root of number is prime or  not.
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
root = math.sqrt(n)

if root.is_integer() and is_prime(int(root)):
    print("The square root of", n, "is prime.")
else:
    print("The square root of", n, "is not prime.")