import pytest

from users.models import User


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(username="testuser")
    assert user.username == "testuser"
