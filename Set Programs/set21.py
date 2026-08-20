#21.	Find students enrolled in both courses and students enrolled in only one course.

python_students = {"Yash", "Prithvi", "Harsh", "Ankit"}
java_students = {"Harsh", "Ankit", "Trisha", "Akash"}

both_courses = python_students & java_students
only_one_course = python_students ^ java_students

print("Students enrolled in Python:", python_students)
print("Students enrolled in Java:", java_students)
print("\nStudents enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)
