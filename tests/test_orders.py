import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.utils import generate_unique_code
from orders.models import Order
from users.models import User


@pytest.mark.django_db
def test_order_creation_with_code():
    user = User.objects.create_user(username="testuser", password="123456")
    order = Order.objects.create(product="Product X", quantity=2, user_id=1)
    assert order.code is not None
    assert len(order.code) == 36  # uuidd length


def test_generate_unique_code():
    code = generate_unique_code()
    assert isinstance(code, str)
    assert len(code) == 36


@pytest.mark.django_db
def test_create_order_api():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="123456")
    client.force_authenticate(user=user)

    url = reverse("order-list")
    data = {"product": "Test Product", "quantity": 3, "user": user.id}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["product"] == "Test Product"
