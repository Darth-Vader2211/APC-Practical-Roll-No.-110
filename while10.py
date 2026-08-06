"""Write a PYTHON program to check the entered number is prime or not"""
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime Number")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")