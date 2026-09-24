class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches

        if inches >= 12:
            feet += inches // 12
            inches = inches % 12

        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")

d1 = Distance(5, 8)
d2 = Distance(4, 7)

d3 = d1 + d2

d3.display()