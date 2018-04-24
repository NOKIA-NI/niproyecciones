from django.db import models

from django.urls import reverse
from . import choices
from estaciones.models import Estacion
from proyecciones.models import Proyeccion
from partes.models import Parte
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

SITIOSLSM45 = '45 sitios LSM'
SITIOSLSM120 = '120 sitios LSM'
SITIOSLSM531 = '531 sitios LSM'
AIRSCALE = 'AIRSCALE'
SI = 'Si'
NO = 'No'

EN_TRANSITO = 'En_Transito'
DESPACHO_SOLICITADO = 'Despacho_Solicitado'

class HwActividad(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='hw_actividades')
    proyeccion = models.OneToOneField(Proyeccion, on_delete=models.CASCADE)
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, related_name='hw_actividades', blank=True, null=True)
    lsm = models.CharField(max_length=255, choices=choices.LSM_CHOICES, blank=True, null=True)
    calculo_hw = models.CharField(max_length=255, choices=choices.CALCULO_HW_CHOICES, default=SI, blank=True, null=True)
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
        if self.estacion.bolsa is not None:
            if self.estacion.bolsa == SITIOSLSM45 or self.estacion.bolsa == SITIOSLSM120 or self.estacion.bolsa == SITIOSLSM531 or self.estacion.bolsa == AIRSCALE:
                self.lsm = SI
            else:
                self.lsm = NO
        if self.lsm is not None:
            if self.lsm == SI:
                self.impactar = NO
            else:
                self.impactar = SI
        if self.impactar == SI and self.estacion.w_fc_sal is None:
            self.impactar = NO
        if self.impactar == SI and self.estacion.mos is not None:
            self.impactar = NO
        if self.impactar == SI and self.estacion.estado_wr == EN_TRANSITO or self.estacion.estado_wr == DESPACHO_SOLICITADO:
            self.impactar = NO

        # if self.parte and self.parte.consumonokia:
        #     consumo_w14 = HwActividad.objects.filter(estacion__w_fc_sal=14, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w15 = HwActividad.objects.filter(estacion__w_fc_sal=15, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w16 = HwActividad.objects.filter(estacion__w_fc_sal=16, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w17 = HwActividad.objects.filter(estacion__w_fc_sal=17, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w18 = HwActividad.objects.filter(estacion__w_fc_sal=18, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w19 = HwActividad.objects.filter(estacion__w_fc_sal=19, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w20 = HwActividad.objects.filter(estacion__w_fc_sal=20, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w21 = HwActividad.objects.filter(estacion__w_fc_sal=21, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w22 = HwActividad.objects.filter(estacion__w_fc_sal=22, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w23 = HwActividad.objects.filter(estacion__w_fc_sal=23, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w24 = HwActividad.objects.filter(estacion__w_fc_sal=24, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w25 = HwActividad.objects.filter(estacion__w_fc_sal=25, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w26 = HwActividad.objects.filter(estacion__w_fc_sal=26, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w27 = HwActividad.objects.filter(estacion__w_fc_sal=27, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w28 = HwActividad.objects.filter(estacion__w_fc_sal=28, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w29 = HwActividad.objects.filter(estacion__w_fc_sal=29, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w30 = HwActividad.objects.filter(estacion__w_fc_sal=30, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w31 = HwActividad.objects.filter(estacion__w_fc_sal=31, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w32 = HwActividad.objects.filter(estacion__w_fc_sal=32, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w33 = HwActividad.objects.filter(estacion__w_fc_sal=33, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w34 = HwActividad.objects.filter(estacion__w_fc_sal=34, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w35 = HwActividad.objects.filter(estacion__w_fc_sal=35, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w36 = HwActividad.objects.filter(estacion__w_fc_sal=36, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w37 = HwActividad.objects.filter(estacion__w_fc_sal=37, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w38 = HwActividad.objects.filter(estacion__w_fc_sal=38, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w39 = HwActividad.objects.filter(estacion__w_fc_sal=39, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w40 = HwActividad.objects.filter(estacion__w_fc_sal=40, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w41 = HwActividad.objects.filter(estacion__w_fc_sal=41, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w42 = HwActividad.objects.filter(estacion__w_fc_sal=42, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w43 = HwActividad.objects.filter(estacion__w_fc_sal=43, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w44 = HwActividad.objects.filter(estacion__w_fc_sal=44, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w45 = HwActividad.objects.filter(estacion__w_fc_sal=45, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w46 = HwActividad.objects.filter(estacion__w_fc_sal=46, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w47 = HwActividad.objects.filter(estacion__w_fc_sal=47, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w48 = HwActividad.objects.filter(estacion__w_fc_sal=48, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w49 = HwActividad.objects.filter(estacion__w_fc_sal=49, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w50 = HwActividad.objects.filter(estacion__w_fc_sal=50, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w51 = HwActividad.objects.filter(estacion__w_fc_sal=51, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #     consumo_w52 = HwActividad.objects.filter(estacion__w_fc_sal=52, parte=self.parte).aggregate(Sum('proyeccion__cantidad_estimada')).get('proyeccion__cantidad_estimada__sum')
        #
        #     if consumo_w14 is not None:
        #         self.parte.consumonokia.w14 = consumo_w14
        #     else:
        #         self.parte.consumonokia.w14 = 0
        #     if consumo_w15 is not None:
        #         self.parte.consumonokia.w15 = consumo_w15
        #     else:
        #         self.parte.consumonokia.w15 = 0
        #     if consumo_w16 is not None:
        #         self.parte.consumonokia.w16 = consumo_w16
        #     else:
        #         self.parte.consumonokia.w16 = 0
        #     if consumo_w17 is not None:
        #         self.parte.consumonokia.w17 = consumo_w17
        #     else:
        #         self.parte.consumonokia.w17 = 0
        #     if consumo_w18 is not None:
        #         self.parte.consumonokia.w18 = consumo_w18
        #     else:
        #         self.parte.consumonokia.w18 = 0
        #     if consumo_w19 is not None:
        #         self.parte.consumonokia.w19 = consumo_w19
        #     else:
        #         self.parte.consumonokia.w19 = 0
        #     if consumo_w20 is not None:
        #         self.parte.consumonokia.w20 = consumo_w20
        #     else:
        #         self.parte.consumonokia.w20 = 0
        #     if consumo_w21 is not None:
        #         self.parte.consumonokia.w21 = consumo_w21
        #     else:
        #         self.parte.consumonokia.w21 = 0
        #     if consumo_w22 is not None:
        #         self.parte.consumonokia.w22 = consumo_w22
        #     else:
        #         self.parte.consumonokia.w22 = 0
        #     if consumo_w23 is not None:
        #         self.parte.consumonokia.w23 = consumo_w23
        #     else:
        #         self.parte.consumonokia.w23 = 0
        #     if consumo_w24 is not None:
        #         self.parte.consumonokia.w24 = consumo_w24
        #     else:
        #         self.parte.consumonokia.w24 = 0
        #     if consumo_w25 is not None:
        #         self.parte.consumonokia.w25 = consumo_w25
        #     else:
        #         self.parte.consumonokia.w25 = 0
        #     if consumo_w26 is not None:
        #         self.parte.consumonokia.w26 = consumo_w26
        #     else:
        #         self.parte.consumonokia.w26 = 0
        #     if consumo_w27 is not None:
        #         self.parte.consumonokia.w27 = consumo_w27
        #     else:
        #         self.parte.consumonokia.w27 = 0
        #     if consumo_w28 is not None:
        #         self.parte.consumonokia.w28 = consumo_w28
        #     else:
        #         self.parte.consumonokia.w28 = 0
        #     if consumo_w29 is not None:
        #         self.parte.consumonokia.w29 = consumo_w29
        #     else:
        #         self.parte.consumonokia.w29 = 0
        #     if consumo_w30 is not None:
        #         self.parte.consumonokia.w30 = consumo_w30
        #     else:
        #         self.parte.consumonokia.w30 = 0
        #     if consumo_w31 is not None:
        #         self.parte.consumonokia.w31 = consumo_w31
        #     else:
        #         self.parte.consumonokia.w31 = 0
        #     if consumo_w32 is not None:
        #         self.parte.consumonokia.w32 = consumo_w32
        #     else:
        #         self.parte.consumonokia.w32 = 0
        #     if consumo_w33 is not None:
        #         self.parte.consumonokia.w33 = consumo_w33
        #     else:
        #         self.parte.consumonokia.w33 = 0
        #     if consumo_w34 is not None:
        #         self.parte.consumonokia.w34 = consumo_w34
        #     else:
        #         self.parte.consumonokia.w34 = 0
        #     if consumo_w35 is not None:
        #         self.parte.consumonokia.w35 = consumo_w35
        #     else:
        #         self.parte.consumonokia.w35 = 0
        #     if consumo_w36 is not None:
        #         self.parte.consumonokia.w36 = consumo_w36
        #     else:
        #         self.parte.consumonokia.w36 = 0
        #     if consumo_w37 is not None:
        #         self.parte.consumonokia.w37 = consumo_w37
        #     else:
        #         self.parte.consumonokia.w37 = 0
        #     if consumo_w38 is not None:
        #         self.parte.consumonokia.w38 = consumo_w38
        #     else:
        #         self.parte.consumonokia.w38 = 0
        #     if consumo_w39 is not None:
        #         self.parte.consumonokia.w39 = consumo_w39
        #     else:
        #         self.parte.consumonokia.w39 = 0
        #     if consumo_w40 is not None:
        #         self.parte.consumonokia.w40 = consumo_w40
        #     else:
        #         self.parte.consumonokia.w40 = 0
        #     if consumo_w41 is not None:
        #         self.parte.consumonokia.w41 = consumo_w41
        #     else:
        #         self.parte.consumonokia.w41 = 0
        #     if consumo_w42 is not None:
        #         self.parte.consumonokia.w42 = consumo_w42
        #     else:
        #         self.parte.consumonokia.w42 = 0
        #     if consumo_w43 is not None:
        #         self.parte.consumonokia.w43 = consumo_w43
        #     else:
        #         self.parte.consumonokia.w43 = 0
        #     if consumo_w44 is not None:
        #         self.parte.consumonokia.w44 = consumo_w44
        #     else:
        #         self.parte.consumonokia.w44 = 0
        #     if consumo_w45 is not None:
        #         self.parte.consumonokia.w45 = consumo_w45
        #     else:
        #         self.parte.consumonokia.w45 = 0
        #     if consumo_w46 is not None:
        #         self.parte.consumonokia.w46 = consumo_w46
        #     else:
        #         self.parte.consumonokia.w46 = 0
        #     if consumo_w47 is not None:
        #         self.parte.consumonokia.w47 = consumo_w47
        #     else:
        #         self.parte.consumonokia.w47 = 0
        #     if consumo_w48 is not None:
        #         self.parte.consumonokia.w48 = consumo_w48
        #     else:
        #         self.parte.consumonokia.w48 = 0
        #     if consumo_w49 is not None:
        #         self.parte.consumonokia.w49 = consumo_w49
        #     else:
        #         self.parte.consumonokia.w49 = 0
        #     if consumo_w50 is not None:
        #         self.parte.consumonokia.w50 = consumo_w50
        #     else:
        #         self.parte.consumonokia.w50 = 0
        #     if consumo_w51 is not None:
        #         self.parte.consumonokia.w51 = consumo_w51
        #     else:
        #         self.parte.consumonokia.w51 = 0
        #     if consumo_w52 is not None:
        #         self.parte.consumonokia.w52 = consumo_w52
        #     else:
        #         self.parte.consumonokia.w52 = 0
        #
        # self.parte.consumonokia.save()

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
