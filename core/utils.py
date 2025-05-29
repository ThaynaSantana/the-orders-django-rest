import uuid

from django.conf import settings
from django.core.mail import send_mail


def generate_unique_code():
    """
    gera codigo uuid4 como string.
    """
    return str(uuid.uuid4())


def send_generic_email(subject: str, message: str, recipient_list: list[str]):
    """
    Envia um email simples.
    """
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )
