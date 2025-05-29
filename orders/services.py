from core.exceptions import ValidationException
from core.utils import generate_unique_code

from .models import Order


def create_order_code():
    return generate_unique_code()


def change_order_status(order_id: int, new_status: str):
    order = Order.objects.filter(id=order_id).first()
    if not order:
        raise ValidationException("Order not found")
    if new_status not in dict(order.ORDER_STATUS):
        raise ValidationException("Invalid status!")
    order.status = new_status
    order.save()
    return order
