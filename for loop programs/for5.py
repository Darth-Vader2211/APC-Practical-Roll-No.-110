#Write a PYTHON program to sum the given sequence
      #1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n! (Factorial of n numbers)
      
n = int(input("Enter the value of n: "))
sum = 0
for i in range(n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum += 1/fact
print("The sum of the sequence is:", sum)