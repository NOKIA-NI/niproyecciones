from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from . import choices

class Consulta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    contenido = models.TextField()
    tipo_consulta = models.CharField(max_length=255, choices=choices.TIPO_CONSULTA_CHOICES, blank=True, null=True)
    data = JSONField()

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'consulta'
        verbose_name_plural = 'consultas'

    def __str__(self):
        return self.nombre

    #  def get_absolute_url(self):
    #     return reverse('consultas:detail_consulta', kwargs={'pk': self.pk})
