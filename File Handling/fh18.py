def read_employees():
    file = open("employees.txt", "r")
    employees = []

    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")
        employees.append([int(emp_id), name, dept, float(salary)])

    file.close()
    return employees


def display_employees(employees):
    for emp in employees:
        print(emp[0], emp[1], emp[2], emp[3])


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])
    print("Highest Paid Employee:")
    print(employee[1], "-", employee[3])


def average_salary(employees):
    total = sum(emp[3] for emp in employees)
    average = total / len(employees)
    print("Average Salary:", average)


def above_salary(employees, salary):
    print("Employees earning above", salary)
    for emp in employees:
        if emp[3] > salary:
            print(emp[1], "-", emp[3])


employees = read_employees()

print("All Employees:")
display_employees(employees)

print()
highest_paid(employees)

print()
average_salary(employees)

print()
above_salary(employees, 55000)