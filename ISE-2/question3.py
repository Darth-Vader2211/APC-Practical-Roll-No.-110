num = int(input("Enter a 3 digit number :"))

first = num // 100
last = num % 10
sum = first + last
print("Sum of first and last digit is :", sum)