"""1.	String Length 
•	Write a program to input a string and display its length without using the len() function. """

str1 = input("Enter a string: ")
count = 0
for i in str1:
    count += 1
print("Length of String = ",count)