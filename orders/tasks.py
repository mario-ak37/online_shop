from celery import shared_task
from decouple import config
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order number: {order.id}"
    message = (
        f"Dear {order.first_name},\n\n"
        f"Thank you for your order! Your order has been placed successfully.\n"
        f"Your order ID is {order.id}.\n\n"
        f"We'll notify you once your order is processed."
    )

    mail_sent = send_mail(
        subject=subject,
        message=message,
        from_email=config("EMAIL_HOST_USER"),
        recipient_list=[order.email],
    )

    return mail_sent
