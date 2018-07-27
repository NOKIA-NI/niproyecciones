from celery import shared_task, current_task
from .models import Proyeccion
from .resources import ProyeccionResource
from django.core.mail import send_mail as _send_mail
from django.core.mail import EmailMessage
from django.utils import timezone

TODAY = timezone.now().date()

@shared_task
def send_mail_proyeccion():
    proyeccion_resource = ProyeccionResource()
    proyeccion = proyeccion_resource.export()
    filename = 'Proyeccion-' + TODAY.strftime('%Y-%m-%d') + '.xlsx'
    content = proyeccion.xlsx
    mimetype = 'application/vnd.ms-excel'
    message = EmailMessage(
        'Proyecciones de Hardware',
        'Proyecciones de Hardware ' + TODAY.strftime('%Y-%m-%d'),
        'notificaciones@nihardware.com',
        [
        'jbri.gap@nokia.com',
        'hw.proyections@nokia.com',
        'administration.hw@nokia.com',
        'hw_control_2.ni@nokia.com',
        'hw_control.ni@nokia.com',
        'csp_support.ni_co@nokia.com',
        'camilo.lozano@nokia.com',
        ],
        )
    message.attach(filename, content, mimetype)
    message.send(fail_silently=False)
    return {'ok':200}
