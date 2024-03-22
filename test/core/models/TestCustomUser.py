import pytest

pytestmark = pytest.mark.django_db


class TestCustomUser:

    def test_email_field(self, custom_user_factory):
        customUser = custom_user_factory()
        assert customUser.email() == 'joao@gmail.com'
