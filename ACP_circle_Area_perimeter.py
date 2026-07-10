
class Circle:
    pi = 3.141592653585
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.pi * self.radius ** 2
    def perimeter(self):
        return 2 * self.pi * self.radius
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())