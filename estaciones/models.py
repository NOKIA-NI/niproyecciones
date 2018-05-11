from django.db import models

from django.urls import reverse
from . import choices
from django.utils import timezone

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == 5 or WEEKDAY == 6 or WEEKDAY == 7:
    WEEK = WEEK + 1

class Estacion(models.Model):
    site_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    region = models.CharField(max_length=255, choices=choices.REGION_CHOICES, blank=True, null=True)
    scope_claro = models.CharField(max_length=255, choices=choices.SCOPE_CHOICES, blank=True, null=True)
    w_fc_imp = models.PositiveIntegerField(blank=True, null=True)
    w_fc_sal = models.PositiveIntegerField(blank=True, null=True)
    total_actividades = models.PositiveIntegerField(blank=True, null=True)
    estado_wr = models.CharField(max_length=255, choices=choices.ESTADO_WR_CHOICES, blank=True, null=True)
    mos = models.DateField(blank=True, null=True)
    bolsa  = models.CharField(max_length=255, choices=choices.BOLSA_CHOICES, blank=True, null=True)
    comunidades  = models.CharField(max_length=255, choices=choices.COMUNIDADES_CHOICES, blank=True, null=True)
    satelital  = models.CharField(max_length=255, choices=choices.SATELITAL_CHOICES, blank=True, null=True)

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
        if self.w_fc_imp is not None:
            self.w_fc_sal = self.w_fc_imp - 3
            if self.w_fc_sal < WEEK:
                self.w_fc_sal = WEEK
        super(Estacion, self).save(*args, **kwargs)
