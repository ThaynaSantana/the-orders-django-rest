import pytest

from users.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username="testuser", password="123456")
    assert user.pk is not None
