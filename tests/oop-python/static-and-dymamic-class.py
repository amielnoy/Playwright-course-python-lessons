class Employee:
    # Static field (class variable)
    company_name = "Tech Corp"

    def __init__(self, name, age):
        # Dynamic fields (instance variables)
        self.name = name
        self.age = age

    def display_info(self):
        """Display employee information."""
        return f"Name: {self.name}, Age: {self.age}, Company: {Employee.company_name}"

    @classmethod
    def change_company_name(cls, new_name):
        """Change the static field company_name."""
        cls.company_name = new_name

# Creating instances of the Employee class
employee1 = Employee("Alice", 30)
employee2 = Employee("Bob", 25)

# Displaying information for each employee
print(employee1.display_info())  # Output: Name: Alice, Age: 30, Company: Tech Corp
print(employee2.display_info())  # Output: Name: Bob, Age: 25, Company: Tech Corp

# Changing the static field company_name
Employee.change_company_name("Innovate Inc.")

# Displaying information again to see the change reflected
print(employee1.display_info())  # Output: Name: Alice, Age: 30, Company: Innovate Inc.
print(employee2.display_info())  # Output: Name: Bob, Age: 25, Company: Innovate Inc.
