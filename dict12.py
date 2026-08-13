#12.	Create a dictionary containing student names and marks. Find the student with the lowest marks.
students = {
    "Yash" :89,
    "Prithvi" : 92,
    "Harsh" : 78,
    "Ankit" : 95,
    "Trisha" : 88
}

values = students.values()
print(values)

lowest_marks = min(values)
for student, marks in students.items():
    if marks == lowest_marks:
        print(f"The student with the lowes marks is {student} with {marks} marks.")