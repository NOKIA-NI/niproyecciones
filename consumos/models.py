from django.db import models

from django.urls import reverse
from . import choices
from partes.models import Parte

class ConsumoNokia(models.Model):
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, related_name='consumos_nokia')
    w14 = models.PositiveIntegerField(blank=True, null=True)
    w15 = models.PositiveIntegerField(blank=True, null=True)
    w16 = models.PositiveIntegerField(blank=True, null=True)
    w17 = models.PositiveIntegerField(blank=True, null=True)
    w18 = models.PositiveIntegerField(blank=True, null=True)
    w19 = models.PositiveIntegerField(blank=True, null=True)
    w20 = models.PositiveIntegerField(blank=True, null=True)
    w21 = models.PositiveIntegerField(blank=True, null=True)
    w22 = models.PositiveIntegerField(blank=True, null=True)
    w23 = models.PositiveIntegerField(blank=True, null=True)
    w24 = models.PositiveIntegerField(blank=True, null=True)
    w25 = models.PositiveIntegerField(blank=True, null=True)
    w26 = models.PositiveIntegerField(blank=True, null=True)
    w27 = models.PositiveIntegerField(blank=True, null=True)
    w28 = models.PositiveIntegerField(blank=True, null=True)
    w29 = models.PositiveIntegerField(blank=True, null=True)
    w30 = models.PositiveIntegerField(blank=True, null=True)
    w31 = models.PositiveIntegerField(blank=True, null=True)
    w32 = models.PositiveIntegerField(blank=True, null=True)
    w33 = models.PositiveIntegerField(blank=True, null=True)
    w34 = models.PositiveIntegerField(blank=True, null=True)
    w35 = models.PositiveIntegerField(blank=True, null=True)
    w36 = models.PositiveIntegerField(blank=True, null=True)
    w37 = models.PositiveIntegerField(blank=True, null=True)
    w38 = models.PositiveIntegerField(blank=True, null=True)
    w39 = models.PositiveIntegerField(blank=True, null=True)
    w40 = models.PositiveIntegerField(blank=True, null=True)
    w41 = models.PositiveIntegerField(blank=True, null=True)
    w42 = models.PositiveIntegerField(blank=True, null=True)
    w43 = models.PositiveIntegerField(blank=True, null=True)
    w44 = models.PositiveIntegerField(blank=True, null=True)
    w45 = models.PositiveIntegerField(blank=True, null=True)
    w46 = models.PositiveIntegerField(blank=True, null=True)
    w47 = models.PositiveIntegerField(blank=True, null=True)
    w48 = models.PositiveIntegerField(blank=True, null=True)
    w49 = models.PositiveIntegerField(blank=True, null=True)
    w50 = models.PositiveIntegerField(blank=True, null=True)
    w51 = models.PositiveIntegerField(blank=True, null=True)
    w52 = models.PositiveIntegerField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'consumo nokia'
        verbose_name_plural = 'consumos nokia'

    def __str__(self):
        return self.parte

    def get_absolute_url(self):
        return reverse('consumos:detail_consumo_nokia', kwargs={'pk': self.pk})

class ConsumoClaro(models.Model):
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, related_name='consumos_claro')
    w14 = models.PositiveIntegerField(blank=True, null=True)
    w15 = models.PositiveIntegerField(blank=True, null=True)
    w16 = models.PositiveIntegerField(blank=True, null=True)
    w17 = models.PositiveIntegerField(blank=True, null=True)
    w18 = models.PositiveIntegerField(blank=True, null=True)
    w19 = models.PositiveIntegerField(blank=True, null=True)
    w20 = models.PositiveIntegerField(blank=True, null=True)
    w21 = models.PositiveIntegerField(blank=True, null=True)
    w22 = models.PositiveIntegerField(blank=True, null=True)
    w23 = models.PositiveIntegerField(blank=True, null=True)
    w24 = models.PositiveIntegerField(blank=True, null=True)
    w25 = models.PositiveIntegerField(blank=True, null=True)
    w26 = models.PositiveIntegerField(blank=True, null=True)
    w27 = models.PositiveIntegerField(blank=True, null=True)
    w28 = models.PositiveIntegerField(blank=True, null=True)
    w29 = models.PositiveIntegerField(blank=True, null=True)
    w30 = models.PositiveIntegerField(blank=True, null=True)
    w31 = models.PositiveIntegerField(blank=True, null=True)
    w32 = models.PositiveIntegerField(blank=True, null=True)
    w33 = models.PositiveIntegerField(blank=True, null=True)
    w34 = models.PositiveIntegerField(blank=True, null=True)
    w35 = models.PositiveIntegerField(blank=True, null=True)
    w36 = models.PositiveIntegerField(blank=True, null=True)
    w37 = models.PositiveIntegerField(blank=True, null=True)
    w38 = models.PositiveIntegerField(blank=True, null=True)
    w39 = models.PositiveIntegerField(blank=True, null=True)
    w40 = models.PositiveIntegerField(blank=True, null=True)
    w41 = models.PositiveIntegerField(blank=True, null=True)
    w42 = models.PositiveIntegerField(blank=True, null=True)
    w43 = models.PositiveIntegerField(blank=True, null=True)
    w44 = models.PositiveIntegerField(blank=True, null=True)
    w45 = models.PositiveIntegerField(blank=True, null=True)
    w46 = models.PositiveIntegerField(blank=True, null=True)
    w47 = models.PositiveIntegerField(blank=True, null=True)
    w48 = models.PositiveIntegerField(blank=True, null=True)
    w49 = models.PositiveIntegerField(blank=True, null=True)
    w50 = models.PositiveIntegerField(blank=True, null=True)
    w51 = models.PositiveIntegerField(blank=True, null=True)
    w52 = models.PositiveIntegerField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'consumo claro'
        verbose_name_plural = 'consumos claro'

    def __str__(self):
        return self.parte

    def get_absolute_url(self):
        return reverse('consumos:detail_consumo_claro', kwargs={'pk': self.pk})
