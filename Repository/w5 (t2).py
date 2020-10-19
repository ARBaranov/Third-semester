class Shape:
    def __init__(self, height, wide):
        self.height = height
        self.wide = wide
class Triangle(Shape):
    def area(self):
        a = (self.height * self.wide)//2
        return a
class Rectangle(Shape):
    def area(self):
        b = (self.wide * self.height)
        return b
a = Triangle(int(input()), int(input()))
b = Rectangle(int(input()), int(input()))

print(a.area(), b.area())