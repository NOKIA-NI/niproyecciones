from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from . import choices
from django.db import connection
from django.core import serializers
import json

class Consulta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    contenido = models.TextField()
    tipo_consulta = models.CharField(max_length=255, choices=choices.TIPO_CONSULTA_CHOICES, blank=True, null=True)
    data = JSONField(blank=True, null=True, editable=False)

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

    def get_absolute_url(self):
        return reverse('consultas:detail_consulta', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.contenido is not None:
            with connection.cursor() as cursor:
                cursor.execute(self.contenido)
                # data = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                print(data)
            self.data = data
            # self.data = json.dumps(data)
        super(Consulta, self).save(*args, **kwargs)
