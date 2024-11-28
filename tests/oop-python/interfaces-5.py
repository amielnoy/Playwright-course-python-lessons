from abc import ABC, abstractmethod

# Define the interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Method to make sound"""
        pass

    @abstractmethod
    def move(self):
        """Method to move"""
        pass

# Implementing the interface in subclasses
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Runs on four legs."

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    def move(self):
        return "Walks gracefully on four legs."

# Function to demonstrate polymorphism
def animal_actions(animal: Animal):
    print(animal.make_sound())
    print(animal.move())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the function with different animals
animal_actions(dog)
animal_actions(cat)
