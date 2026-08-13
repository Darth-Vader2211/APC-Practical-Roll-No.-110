#1.	Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
student = {
    "roll_number": 12345,
    "name": "Alice",
    "department": "Computer Science",
    "marks": 85
}

for key, value in student.items():
    print(f"{key}: {value}")