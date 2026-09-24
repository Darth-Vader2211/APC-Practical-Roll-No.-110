class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print()


s1 = Student(1, "Yash", [85, 90, 78, 88, 92])
s2 = Student(2, "Rahul", [75, 82, 80, 79, 85])
s3 = Student(3, "Amit", [90, 85, 88, 92, 95])

s1.display()
s2.display()
s3.display()