"""Create a class named Circle and intialize it with radius. Make two methods
getArea (to return area of a circle) and getCircumference (to return the
circumference of the circle )inside this class."""
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        area = math.pi * self.radius ** 2
        return area

    def getCircumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference

circle = Circle(14)
print(f"This your Area {circle.getArea()}")
print(f"This your circumference {circle.getCircumference()}")




