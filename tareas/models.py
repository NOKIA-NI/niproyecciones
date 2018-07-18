from django.db import models
from django.urls import reverse

class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ejecutar = models.CharField(max_length=255)
    tarea_id = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('tareas:detail_tarea', kwargs={'pk': self.pk})
