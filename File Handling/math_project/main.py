from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import prime, armstrong, palindrome
from mathutils.statistics import mean, maximum, minimum

a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))

n = 153

print("\nNumber:", n)
print("Prime:", prime(n))
print("Armstrong:", armstrong(n))
print("Palindrome:", palindrome(n))

numbers = [10, 20, 30, 40, 50]

print("\nMean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))