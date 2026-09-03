employees = [
    ("Amit", 45000),
    ("Rahul", 60000),
    ("Sneha", 50000),
    ("Riya", 75000)
]

result = sorted(employees, key=lambda employee: employee[1])

print(result)