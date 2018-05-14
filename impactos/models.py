from django.db import models
from estaciones.models import Estacion
from partes.models import Parte
from . import choices
from partes import choices as partes_choices
from estaciones import choices as estaciones_choices

class Impacto(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, blank=True, null=True, related_name='impactos')
    w_fc_sal = models.PositiveIntegerField(blank=True, null=True)
    w_fc_imp = models.PositiveIntegerField(blank=True, null=True)
    bolsa = models.CharField(max_length=255, choices=estaciones_choices.BOLSA_CHOICES, blank=True, null=True)
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, blank=True, null=True, related_name='impactos')
    grupo_parte = models.CharField(max_length=255, choices=partes_choices.GRUPO_PARTE_CHOICES, blank=True, null=True)
    cantidad_estimada = models.PositiveIntegerField(blank=True, null=True)
    tipo_impacto = models.CharField(max_length=255, choices=choices.TIPO_IMPACTO_CHOICES, blank=True, null=True)
    impactado = models.CharField(max_length=255, choices=choices.IMPACTADO_CHOICES, default='No', blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'impacto'
        verbose_name_plural = 'impactos'

    def __str__(self):
        return self.estacion.site_name

    # def get_absolute_url(self):
    #     return reverse('estaciones:detail_estacion', kwargs={'pk': self.pk})
