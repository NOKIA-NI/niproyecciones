from django.db import models

from django.urls import reverse
from . import choices

class Estacion(models.Model):
    site_name = models.CharField(max_length=255, unique=True)
    region = models.CharField(max_length=255, choices=choices.REGION_CHOICES)
    scope_claro = models.CharField(max_length=255, choices=choices.SCOPE_CHOICES, blank=True, null=True)
    w_fc_imp = models.PositiveIntegerField(blank=True, null=True)
    total_actividades = models.PositiveIntegerField(blank=True, null=True)
    estado_wr = models.CharField(max_length=255, choices=choices.ESTADO_WR_CHOICES, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "estacion"
        verbose_name_plural = "estaciones"

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse('estaciones:detail_estacion', kwargs={'pk': self.pk})
