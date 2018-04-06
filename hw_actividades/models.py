from django.db import models

from django.urls import reverse
from . import choices
from estaciones.models import Estacion
from proyecciones.models import Proyeccion
from partes.models import Parte
from django.db.models.signals import post_save
from django.dispatch import receiver

SI = 'Si'
NO = 'No'

class HwActividad(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='hw_actividades')
    proyeccion = models.OneToOneField(Proyeccion, on_delete=models.CASCADE)
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, related_name='hw_actividades')
    lsm = models.CharField(max_length=255, choices=choices.LSM_CHOICES, blank=True, null=True)
    calculo_hw = models.CharField(max_length=255, choices=choices.CALCULO_HW_CHOICES, blank=True, null=True)
    impactar = models.CharField(max_length=255, choices=choices.IMPACTAR_CHOICES, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'hw actividad'
        verbose_name_plural = 'hw actividades'

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('hw_actividades:detail_hw_actividad', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.estacion.w_fc_imp is not None:
            if self.lsm == SI:
                self.impactar = SI
            else:
                self.impactar = NO
        super(HwActividad, self).save(*args, **kwargs)

    @receiver(post_save, sender=Proyeccion)
    def create_hw_actividad(sender, instance, created, **kwargs):
        if created:
            hw_actividad, new = HwActividad.objects.get_or_create(estacion=instance.estacion,
                                                                  proyeccion=instance,
                                                                  parte=instance.parte)

    @receiver(post_save, sender=Proyeccion)
    def save_hw_actividad(sender, instance, **kwargs):
        instance.hwactividad.estacion = instance.estacion
        instance.hwactividad.parte = instance.parte
        instance.hwactividad.save()
