'''Write a PYTHON program to compute the cosine series
          cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!'''
          
n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
sum = 0
for i in range(n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum += ((-1)**i)*(x**(2*i))/fact
print("The value of cos(", x, ") is:", sum)