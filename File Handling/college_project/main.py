from student.details import student_details
from student.marks import display_marks
from faculty.details import faculty_details

print("STUDENT INFORMATION")

student_details("Amit", 101, "Computer Engineering")

display_marks([85, 90, 78, 88, 92])

print("\nFACULTY INFORMATION")

faculty_details("Dr. Patil", "Computer Engineering", 10)