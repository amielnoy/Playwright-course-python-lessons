class Car:
    def __init__(self, make, model, year):
        self.make = make      # Instance variable for car make
        self.model = model    # Instance variable for car model
        self.year = year      # Instance variable for car year

    def display_info(self):
        """Method to display information about the car."""
        return f"{self.year} {self.make} {self.model}"

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

# Displaying information about each car
print(car1.display_info())  # Output: 2020 Toyota Corolla
print(car2.display_info())  # Output: 2019 Honda Civic
print("\n\n\n")

# ********************************Modify instance vars************************************************
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Instance variable for account holder's name
        self.balance = balance                  # Instance variable for account balance

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount."

# Creating an instance of BankAccount
account = BankAccount("Alice", 1000)

# Performing transactions
print(account.deposit(500))   # Output: Deposited $500. New balance: $1500
print(account.withdraw(200))  # Output: Withdrew $200. New balance: $1300
print(account.withdraw(1500)) # Output: Insufficient funds or invalid amount.



print("\n\n\n")
# ************************inheritance*********************
class Animal:
    def __init__(self, name):
        self.name = name  # Instance variable for animal name

    def speak(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method on each animal
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!


