"""Write a PYTHON program to produce following design
       A B C D E
       A B C D
       A B C
       A B
       A """
n = int(input("Enter a number :"))
for i in range(n, 0,-1):
    for j in range(n):
        if j < i:
            print(chr(65+j),end = " ")
    print()