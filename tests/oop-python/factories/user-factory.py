# factories.py
import factory
from factory import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
