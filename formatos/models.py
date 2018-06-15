from django.db import models
from estaciones.models import Estacion
from partes.models import Parte

class FormatoEstacion(models.Model):
    estacion = models.OneToOneField(Estacion, on_delete=models.CASCADE, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'formato estacion'
        verbose_name_plural = 'formatos estacion'

    def __str__(self):
        return self.estacion.site_name

    # def get_absolute_url(self):
    #     return reverse('estaciones:detail_estacion', kwargs={'pk': self.pk})

class FormatoParte(models.Model):
    formato_estacion = models.ForeignKey(FormatoEstacion, on_delete=models.CASCADE, related_name='formatos_parte', blank=True, null=True)
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, related_name='formatos_parte', blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'formato parte'
        verbose_name_plural = 'formatos parte'
        unique_together = ('formato_estacion', 'parte')

    def __str__(self):
        return self.parte.parte_nokia

    # def get_absolute_url(self):
    #     return reverse('estaciones:detail_estacion', kwargs={'pk': self.pk})


