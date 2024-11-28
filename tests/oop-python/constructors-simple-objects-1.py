class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Roll No.: {self.roll_no}, Name: {self.name}")

# Creating objects of the class
student1 = Student("Alice", 1)
student2 = Student("Bob", 2)

student1.display()
student2.display()
