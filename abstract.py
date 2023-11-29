from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
circle = Circle(radius=8)
rectangle = Rectangle(length=4, width=6)

print(f"Area of Circle: {circle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")
