from django.db import models
from django.urls import reverse
from . import choices
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from users.models import Perfil
from django.db.models.signals import post_save
from django.dispatch import receiver

GRUPOHW = 'Grupo HW'

class Rastreo(models.Model):
    responsable = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='rastreos')
    nombre = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'rastreo'
        verbose_name_plural = 'rastreos'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('rastreos:detail_rastreo', kwargs={'pk': self.pk})


class Proceso(models.Model):
    rastreo = models.ForeignKey(Rastreo, on_delete=models.CASCADE, blank=True, null=True, related_name='procesos')
    responsable = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='procesos')
    tipo_proceso = models.CharField(max_length=255, choices=choices.TIPO_PROCESO_CHOICES, blank=True, null=True)
    estado_proceso = models.CharField(max_length=255, choices=choices.ESTADO_PROCESO_CHOICES, default='Abierto', blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to='procesos/archivos/%Y-%m-%d/', blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'proceso'
        verbose_name_plural = 'procesos'

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse('rastreos:detail_proceso', kwargs={'pk': self.pk})

    @receiver(post_save, sender=Rastreo)
    def create_proceso(sender, instance, created, **kwargs):
        if created:
            proceso, new = Proceso.objects.get_or_create(rastreo=instance,
                                                          responsable=instance.responsable,
                                                          tipo_proceso=GRUPOHW,)

    # @receiver(post_save, sender=Rastreo)
    # def save_proceso(sender, instance, **kwargs):
    #     instance.save()
    
