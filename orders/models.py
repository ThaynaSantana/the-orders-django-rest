from django.conf import settings
from django.db import models

from core.constants import ORDER_STATUS


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default="pending")
    code = models.CharField(max_length=36, unique=True, editable=True)

    def __str__(self):
        return "f{self.product} x{self.quantity} by {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.code:
            from core.utils import generate_unique_code

            self.code = generate_unique_code()
        super().save(*args, **kwargs)
