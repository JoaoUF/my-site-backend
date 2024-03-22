import factory
from core.models.CustomUser import CustomUser
# from core.models.Item import Item


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = 'joao@gmail.com'
    password = '123456'
    is_superuser = True
    is_staff = True


# class ItemFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Item
#
#     name = 'causa'
#     description = 'causa rellena'
#     price = 55
#     usuarioAdicion = factory.SubFactory(CustomUserFactory)
