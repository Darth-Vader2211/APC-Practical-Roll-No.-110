"""Write a PYTHON program to produce following design
      A
      A B
      A B C
      A B C D 
      A B C D E
      If user enters n value as 5"""
n = int(input("Enter a number: "))
for i in range(n):
      for j in range(i+1):
            print(chr (65+j),end = " ")
      print()
