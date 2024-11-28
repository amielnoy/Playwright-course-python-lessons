
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
#print(vars(person))

# This will output: {'name': 'Alice', 'age': 30}12
# Examples and Exercises
# Example 1: vars() with no arguments
# When called without arguments, vars() returns a dictionary of the current local symbol table.

x = 10
y = "Hello"
def test_vars1():
    print(f"x={x},y={y}")

x_float = 10.92
y_float = 1234.35
def test_vars_float():
    print(f"x_float={x_float},y_float={y_float}")
# This will output a dictionary containing all local variables, including 'x' and 'y'1.
# Exercise 1: Create three variables with different types (integer, string, list) and then use vars() to display all local variables. What do you observe?
# Example 2: vars() with a custom object

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(vars(my_car))

# This will output: {'brand': 'Toyota', 'model': 'Corolla'}1
# Exercise 2: Create a class called Student with attributes for name, age, and grade. Create an instance of this class and use vars() to display its attributes.
# Example 3: vars() with built-in types
# python
print(vars(list))
print(vars(dict))

# This will output the attributes of the list and dict classes1.
# Exercise 3: Use vars() on different built-in types (e.g., str, int, float) and compare the outputs. What differences do you notice?
# Example 4: vars() with modules
# You can use vars() with imported modules to see their attributes.
# python
import math
print(vars(math))

# This will output a dictionary of all attributes and functions in the math module.
# Exercise 4: Import the random module and use vars() to display its attributes. Can you identify some familiar random-related functions?
# Example 5: Modifying object attributes
# python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(5, 10)
vars(rect)['color'] = 'red'
print(vars(rect))

# This will output: {'width': 5, 'height': 10, 'color': 'red'}

# Exercise 5: Create a class called Book with attributes for title and author. Create an instance of this class, use vars() to add a new attribute 'year', and then print the updated attributes.
# Remember, vars() is particularly useful for introspection and debugging, allowing you to examine the attributes of objects dynamically. It's important to note that not all objects have a __dict__ attribute, and vars() will raise a TypeError if used on such objects