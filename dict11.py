#11.	Create a dictionary containing student names and marks. Find the student who has scored the highest marks.

students = {
    "Yash" :89,
    "Prithvi" : 92,
    "Harsh" : 78,
    "Ankit" : 95,
    "Trisha" : 88
}

values = students.values()
print(values)

highest_marks = max(values)
for student, marks in students.items():
    if marks == highest_marks:
        print(f"The student with the highest marks is {student} with {marks} marks.")