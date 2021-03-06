from django.db import models
from django.urls import reverse
from . import choices
from django.utils import timezone
from partes.models import Parte
from django.conf import settings

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == settings.VIERNES or WEEKDAY == settings.SABADO or WEEKDAY == settings.DOMINGO:
    WEEK = WEEK + 1

class Estacion(models.Model):
    site_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    region = models.CharField(max_length=255, choices=choices.REGION_CHOICES, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    scope_claro = models.CharField(max_length=255, choices=choices.SCOPE_CHOICES, blank=True, null=True)
    w_fc_sal = models.PositiveIntegerField(blank=True, null=True)
    w_fc_imp = models.PositiveIntegerField(blank=True, null=True)
    w_fc_c = models.PositiveIntegerField(blank=True, null=True)
    total_actividades = models.PositiveIntegerField(blank=True, null=True)
    estado_wr = models.CharField(max_length=255, choices=choices.ESTADO_WR_CHOICES, blank=True, null=True)
    mos = models.DateField(blank=True, null=True)
    bolsa = models.CharField(max_length=255, choices=choices.BOLSA_CHOICES, blank=True, null=True)
    status_nokia = models.CharField(max_length=255, choices=choices.STATUS_NOKIA_CHOICES, blank=True, null=True)
    comunidades = models.CharField(max_length=255, choices=choices.COMUNIDADES_CHOICES, blank=True, null=True)
    satelital  = models.CharField(max_length=255, choices=choices.SATELITAL_CHOICES, blank=True, null=True)
    impactar = models.CharField(max_length=255, choices=choices.IMPACTAR_CHOICES, default='Si')
    partes = models.ManyToManyField(Parte, blank=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'estacion'
        verbose_name_plural = 'estaciones'

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse('estaciones:detail_estacion', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.w_fc_c is not None:
            self.w_fc_imp = self.w_fc_c
        if self.w_fc_imp is None:
            self.w_fc_sal = self.w_fc_imp
        if self.w_fc_imp is not None and self.mos is not None:
            self.w_fc_sal = self.mos.isocalendar()[1]
        if (self.w_fc_imp is not None and self.w_fc_imp >= WEEK) and self.mos is None:
            self.w_fc_sal = self.w_fc_imp - 3
            if self.w_fc_sal < WEEK:
                self.w_fc_sal = WEEK
        if (self.w_fc_imp is not None and self.w_fc_imp < WEEK) and self.mos is None:
            self.w_fc_sal = self.w_fc_imp
        super(Estacion, self).save(*args, **kwargs)

class BitacoraEstacion(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='bitacoras_estacion', blank=True, null=True)
    fecha_bitacora = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'bitacora estacion'
        verbose_name_plural = 'bitacoras estacion'

    def __str__(self):
        return self.estacion.site_name

    def get_absolute_url(self):
        return reverse('estaciones:detail_bitacora_estacion', kwargs={'pk': self.pk})

class ProyeccionEstacion(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='proyecciones_estacion', blank=True, null=True)
    proyeccion = models.CharField(max_length=255, choices=choices.PROYECCION_CHOICES, blank=True, null=True)
    fecha_proyeccion = models.DateField(auto_now_add=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'proyecion estacion'
        verbose_name_plural = 'proyeciones estacion'

    def __str__(self):
        return self.estacion.site_name

    # def get_absolute_url(self):
    #     return reverse('estaciones:detail_estacion_proyeccion', kwargs={'pk': self.pk})
