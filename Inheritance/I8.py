class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.40


class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20


m = Manager(101, "A", 50000)
d = Developer(102, "B", 50000)
t = Tester(103, "C", 50000)

print("Manager Salary:", m.salary())
print("Developer Salary:", d.salary())
print("Tester Salary:", t.salary())