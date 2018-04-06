from django.db import models

from django.urls import reverse
from . import choices

class Parte(models.Model):
    cod_sap = models.PositiveIntegerField(blank=True, null=True)
    parte_nokia = models.CharField(max_length=255, blank=True, null=True)
    capex = models.CharField(max_length=255, blank=True, null=True)
    grupo_parte = models.CharField(max_length=255, choices=choices.GRUPO_PARTE_CHOICES, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'parte'
        verbose_name_plural = 'partes'

    def __str__(self):
        return self.parte_nokia

    def get_absolute_url(self):
        return reverse('partes:detail_parte', kwargs={'pk': self.pk})
