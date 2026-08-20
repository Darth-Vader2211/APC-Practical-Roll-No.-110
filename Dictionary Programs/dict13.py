#13.	Create a dictionary containing student names and marks. Calculate the average marks of all students.

students = {
    "Yash" :89,
    "Prithvi" : 92,
    "Harsh" : 78,
    "Ankit" : 95,
    "Trisha" : 88
}

values = students.values()
print(values)

average_marks = sum(values)/len(values)
print(f"The average marks of all students is {average_marks}.")