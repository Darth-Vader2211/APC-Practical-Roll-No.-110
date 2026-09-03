students = [
    ("Yash", 85),
    ("Rahul", 72),
    ("Amit", 91),
    ("Riya", 78)
]

result = sorted(students, key=lambda student: student[1])

print(result)