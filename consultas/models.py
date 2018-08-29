from django.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from . import choices
from django.db import connection, connections
from django.core import serializers
import json

class Consulta(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    tipo_consulta = models.CharField(max_length=255, choices=choices.TIPO_CONSULTA_CHOICES, default='Custom')
    database = models.CharField(max_length=255, choices=choices.DATABASE_CHOICES, default='default')
    contenido = models.TextField()
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
        data = ''
        if self.tipo_consulta == 'Custom':
            if self.contenido is not None:
                if self.database:
                    with connections[self.database].cursor() as cursor:
                        cursor.execute(self.contenido)
                        columns = [col[0] for col in cursor.description]
                        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                else:
                    with connection.cursor() as cursor:
                        cursor.execute(self.contenido)
                        columns = [col[0] for col in cursor.description]
                        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                self.data = json.dumps(data, default=str)
        if self.tipo_consulta == 'Raw':
            pass
        super(Consulta, self).save(*args, **kwargs)
