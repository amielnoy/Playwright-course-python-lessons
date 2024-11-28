class Student:
    def __init__(self, name="Unknown", roll_no=0):
        self.name = name
        self.roll_no = roll_no

student1 = Student("Alice", 1)
student2 = Student()  # Uses default values

print(f"Student 1: Name={student1.name}, Roll No={student1.roll_no}")
print(f"Student 2: Name={student2.name}, Roll No={student2.roll_no}")
