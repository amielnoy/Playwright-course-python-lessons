# test_user.py
def test_user_creation(user_factory):
    user = user_factory(username="testuser", email="test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"

def test_user_greeting(user_factory):
    user = user_factory(username="alice")
    assert user.greet() == "Hello, alice!"
