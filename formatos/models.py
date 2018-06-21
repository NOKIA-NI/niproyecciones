from django.db import models
from estaciones.models import Estacion
from partes.models import Parte
from . import choices
from estaciones import choices as estaciones_choices
import datetime

MONTH = datetime.datetime.now().strftime("%B")
if MONTH == 'January':
    MONTH = 'Enero'
if MONTH == 'February':
    MONTH = 'Febrero'
if MONTH == 'March':
    MONTH = 'Marzo'
if MONTH == 'April':
    MONTH = 'Abril'
if MONTH == 'May':
    MONTH = 'Mayo'
if MONTH == 'June':
    MONTH = 'Junio'
if MONTH == 'July':
    MONTH = 'Julio'
if MONTH == 'August':
    MONTH = 'Agosto'
if MONTH == 'September':
    MONTH = 'Septiembre'
if MONTH == 'November':
    MONTH = 'Noviembre'
if MONTH == 'December':
    MONTH = 'Diciembre'

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
    #     return reverse('formatos:detail_estacion', kwargs={'pk': self.pk})

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
    #     return reverse('formatos:detail_estacion', kwargs={'pk': self.pk})


class FormatoClaro(models.Model):
    formato_parte = models.ForeignKey(FormatoParte, on_delete=models.CASCADE, related_name='formatos_claro', blank=True, null=True)
    sitio = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='formatos_claro', blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    sap = models.PositiveIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    regional = models.CharField(max_length=255, choices=estaciones_choices.REGION_CHOICES, blank=True, null=True)
    semana = models.PositiveIntegerField(blank=True, null=True)
    mes = models.CharField(max_length=255, choices=choices.MES_CHOICES, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'formato claro'
        verbose_name_plural = 'formatos claro'

    def __str__(self):
        return self.formato_parte.formato_estacion.estacion.site_name

    # def get_absolute_url(self):
    #     return reverse('formatos:detail_estacion', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        
        self.sitio = self.formato_parte.formato_estacion.estacion
        self.sap = self.formato_parte.parte.cod_sap
        self.descripcion = self.formato_parte.parte.capex
        self.qty = self.formato_parte.cantidad
        self.ciudad = self.formato_parte.formato_estacion.estacion.ciudad
        self.regional = self.formato_parte.formato_estacion.estacion.region
        self.semana = self.formato_parte.formato_estacion.estacion.w_fc_sal
        self.mes = MONTH
        
        super(FormatoClaro, self).save(*args, **kwargs)


