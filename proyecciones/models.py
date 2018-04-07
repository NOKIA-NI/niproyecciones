from django.db import models

from django.urls import reverse
from . import choices
from estaciones.models import Estacion
from partes.models import Parte

class Proyeccion(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='proyecciones')
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    escenario = models.CharField(max_length=255, blank=True, null=True)
    banda = models.CharField(max_length=255, blank=True, null=True)
    agrupadores = models.CharField(max_length=255, blank=True, null=True)
    rfe = models.DateField(blank=True, null=True)
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, related_name='proyecciones', blank=True, null=True)
    estado_proyeccion  = models.CharField(max_length=255, choices=choices.ESTADO_PROYECCION_CHOICES)
    cantidad_estimada = models.PositiveIntegerField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'proyeccion'
        verbose_name_plural = 'proyecciones'

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('proyecciones:detail_proyeccion', kwargs={'pk': self.pk})
