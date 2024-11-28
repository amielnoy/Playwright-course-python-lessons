class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

employee1 = Employee("John", 25)
employee2 = Employee("Jane", 28)

print(f"Name: {employee1.name}, Age: {employee1.age}")
print(f"Name: {employee2.name}, Age: {employee2.age}")
