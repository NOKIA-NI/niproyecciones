from celery import shared_task
from django.core.mail import send_mail as _send_mail

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def send_mail():
    _send_mail(
    'Test Email',
    'This is a Test Email',
    'notificaciones@nihardware.com',
    ['jbri.gap@nokia.com', 'jucebridu@gmail.com'],
    fail_silently=False,
    )