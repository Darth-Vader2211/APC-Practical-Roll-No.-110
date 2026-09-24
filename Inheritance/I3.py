class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def performance(self):
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", self.marks + self.sports_points)


s = Student(85, 15)
s.performance()