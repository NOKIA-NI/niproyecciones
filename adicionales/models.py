from django.db import models
from django.urls import reverse
from users.models import Perfil
from . import choices
from django.utils import timezone

TODAY = timezone.now()

class Adicional(models.Model):
    idadicionales_hw_sv = models.PositiveIntegerField(primary_key=True)
    wp = models.BigIntegerField(blank=True, null=True)
    siteName = models.CharField(max_length=60, blank=True, null=True)
    proyecto = models.CharField(max_length=45, blank=True, null=True)
    banda = models.CharField(max_length=45, blank=True, null=True)
    escenario = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    seccion = models.CharField(max_length=20, blank=True, null=True)
    parte = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    proceso = models.CharField(max_length=210, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_pedido = models.DateTimeField(blank=True, null=True)
    usuario = models.CharField(max_length=45, blank=True, null=True)
    id = models.PositiveIntegerField(blank=True, null=True)

    recibido = models.CharField(max_length=255, choices=choices.RECIBIDO_CHOICES, default='No', null=True)
    fecha_recibido = models.DateTimeField(blank=True, null=True)
    responsable = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='adicionales', blank=True, null=True)
    asignado = models.CharField(max_length=255, choices=choices.ASIGNADO_CHOICES, default='No', null=True)
    fecha_asignado = models.DateTimeField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    # estado = models.BooleanField(default=True, editable=False)
    # subestado = models.BooleanField(default=False, editable=False)
    # creado = models.DateTimeField(auto_now_add=True)
    # actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-fecha_pedido',)
        verbose_name = 'adicional'
        verbose_name_plural = 'adicionales'

    def __str__(self):
        return str(self.idadicionales_hw_sv)

    # def get_absolute_url(self):
    #     return reverse('adicionales:detail_adicional', kwargs={'pk': self.pk})
