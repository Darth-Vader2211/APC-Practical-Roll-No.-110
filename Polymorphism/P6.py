class Student:
    def calculate_grade(self, marks):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"

class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "Distinction"
        elif marks >= 60:
            return "First Class"
        elif marks >= 50:
            return "Pass"
        else:
            return "Fail"

class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            return "A"
        elif marks >= 55:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "F"

students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print(student.calculate_grade(75))