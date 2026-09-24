class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 80000

class Developer(Employee):
    def calculate_salary(self):
        return 60000

class Tester(Employee):
    def calculate_salary(self):
        return 45000

employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print("Salary:", employee.calculate_salary())