# user.py
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self):
        return f"Hello, {self.username}!"

