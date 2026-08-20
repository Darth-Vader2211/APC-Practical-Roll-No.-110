#4.	Create a dictionary containing student marks. Update the marks of a specified student.
student_marks = {
    "Yash": 85,
    "Prithvi": 90,
    "Harsh": 78,
    "Ankit": 92,
    "Trisha": 88
}
student_name = input("Enter the name of the student to update marks: ")
if student_name in student_marks:
    new_marks = int(input(f"Enter the new marks for the Student: "))
    student_marks[student_name] = new_marks
    print(f"Updated marks for {student_name}: {student_marks[student_name]}")
else:
    print("Student not found.")