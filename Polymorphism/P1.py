class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        r = 5
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 5
        return l * b

class Triangle(Shape):
    def area(self):
        b = 10
        h = 6
        return 0.5 * b * h

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    print("Area:", shape.area())