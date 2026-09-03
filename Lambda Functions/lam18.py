employees = [
    ("Yash", "IT", 60000),
    ("Rahul", "HR", 45000),
    ("Amit", "IT", 75000),
    ("Riya", "Finance", 55000)
]

# a) Employees earning more than 50000
high_salary = list(
    filter(lambda employee: employee[2] > 50000, employees)
)

# b) Increase salary by 10%
increased_salary = list(
    map(lambda employee: (
        employee[0],
        employee[1],
        employee[2] * 1.10
    ), employees)
)

# c) Sort according to salary
sorted_employees = sorted(
    employees,
    key=lambda employee: employee[2]
)

print("Above 50000:", high_salary)
print("After 10% increase:", increased_salary)
print("Sorted:", sorted_employees)