#10.	Create a tuple of 10 numbers and display:
#	•	First five elements 
#	•	Last five elements 
#	•	Middle four elements 
#	•	Alternate elements 
#	•	Reverse tuple

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

first_five = numbers[:5]
last_five = numbers[-5:]
middle_four = numbers[3:7]
alternate_elements = numbers[::2]
reversed_tuple = numbers[::-1]

print("Original tuple:", numbers)
print("First five elements:", first_five)
print("Last five elements:", last_five)
print("Middle four elements:", middle_four)
print("Alternate elements:", alternate_elements)
print("Reversed tuple:", reversed_tuple)
