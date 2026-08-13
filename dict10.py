#10.	Accept five student names and their marks from the user and store them in a dictionary.

students = {}
for i in range(5):
    name = input(f"Enter the name of student {i + 1}: ")
    marks = int(input(f"Enter the marks of {name}: "))
    students[name] = marks

print("Student Data:")
for name, marks in students.items():
    print(f"{name}: {marks}")