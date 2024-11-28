class MathUtils:
    @staticmethod
    def add(x, y):
        """Returns the sum of x and y."""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Returns the difference of x and y."""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Returns the product of x and y."""
        return x * y

    @staticmethod
    def divide(x, y):
        """Returns the quotient of x and y. Raises an error if dividing by zero."""
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

# Using the static methods without creating an instance of MathUtils
print(MathUtils.add(10, 5))         # Output: 15
print(MathUtils.subtract(10, 5))    # Output: 5
print(MathUtils.multiply(10, 5))     # Output: 50
print(MathUtils.divide(10, 5))       # Output: 2.0

# Attempting to divide by zero
try:
    print(MathUtils.divide(10, 0))
except ValueError as e:
    print(e)  # Output: Cannot divide by zero.
