from pytest_factoryboy import register
from .factories import CustomUserFactory

# register(ItemFactory)
register(CustomUserFactory)