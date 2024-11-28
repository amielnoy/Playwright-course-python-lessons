from abc import ABC, abstractmethod

# Define the interface
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

# Implementing the interface in subclasses
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Function to demonstrate polymorphism
def print_shape_info(shape: Shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Creating instances of Rectangle and Circle
shapes = [
    Rectangle(10, 5),
    Circle(7)
]

# Iterating through the collection and printing their info
for shape in shapes:
    print_shape_info(shape)
