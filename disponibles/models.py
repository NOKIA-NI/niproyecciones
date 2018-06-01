from django.db import models

from django.urls import reverse
from partes import choices
from partes.models import Parte
from django.db.models.signals import post_save
from django.dispatch import receiver
from consumos.models import ConsumoNokia, ConsumoClaro
from llegadas.models import Llegada
from django.utils import timezone
from django.conf import settings

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]
WEEKDAY = TODAY.weekday()
if WEEKDAY == settings.VIERNES or WEEKDAY == settings.SABADO or WEEKDAY == settings.DOMINGO:
    WEEK = WEEK + 1

class Disponible(models.Model):
    parte = models.OneToOneField(Parte, on_delete=models.CASCADE)
    grupo_parte = models.CharField(max_length=255, choices=choices.GRUPO_PARTE_CHOICES, blank=True, null=True)
    w14 = models.IntegerField(default=0)
    w15 = models.IntegerField(default=0)
    w16 = models.IntegerField(default=0)
    w17 = models.IntegerField(default=0)
    w18 = models.IntegerField(default=0)
    w19 = models.IntegerField(default=0)
    w20 = models.IntegerField(default=0)
    w21 = models.IntegerField(default=0)
    w22 = models.IntegerField(default=0)
    w23 = models.IntegerField(default=0)
    w24 = models.IntegerField(default=0)
    w25 = models.IntegerField(default=0)
    w26 = models.IntegerField(default=0)
    w27 = models.IntegerField(default=0)
    w28 = models.IntegerField(default=0)
    w29 = models.IntegerField(default=0)
    w30 = models.IntegerField(default=0)
    w31 = models.IntegerField(default=0)
    w32 = models.IntegerField(default=0)
    w33 = models.IntegerField(default=0)
    w34 = models.IntegerField(default=0)
    w35 = models.IntegerField(default=0)
    w36 = models.IntegerField(default=0)
    w37 = models.IntegerField(default=0)
    w38 = models.IntegerField(default=0)
    w39 = models.IntegerField(default=0)
    w40 = models.IntegerField(default=0)
    w41 = models.IntegerField(default=0)
    w42 = models.IntegerField(default=0)
    w43 = models.IntegerField(default=0)
    w44 = models.IntegerField(default=0)
    w45 = models.IntegerField(default=0)
    w46 = models.IntegerField(default=0)
    w47 = models.IntegerField(default=0)
    w48 = models.IntegerField(default=0)
    w49 = models.IntegerField(default=0)
    w50 = models.IntegerField(default=0)
    w51 = models.IntegerField(default=0)
    w52 = models.IntegerField(default=0)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'disponible'
        verbose_name_plural = 'disponibles'

    def __str__(self):
        return self.parte.parte_nokia

    def get_absolute_url(self):
        return reverse('disponibles:detail_disponible', kwargs={'pk': self.pk})

    @receiver(post_save, sender=Parte)
    def create_disponible(sender, instance, created, **kwargs):
        if created:
            disponible, new = Disponible.objects.get_or_create(parte=instance,
                                                               grupo_parte=instance.grupo_parte)

    @receiver(post_save, sender=Parte)
    def save_disponible(sender, instance, **kwargs):
        instance.disponible.grupo_parte = instance.grupo_parte
        instance.disponible.save()

    @receiver(post_save, sender=ConsumoNokia)
    @receiver(post_save, sender=ConsumoClaro)
    @receiver(post_save, sender=Llegada)
    def calculate_disponible(sender, instance, **kwargs):
        try:
            if instance.parte and instance.parte.consumonokia and instance.parte.consumoclaro and instance.parte.llegada and instance.parte.disponible:
                disponible_w14 = (instance.parte.resultado.w14 + instance.parte.llegada.w14) - (instance.parte.consumonokia.w14 + instance.parte.consumoclaro.w14)
                disponible_w15 = (instance.parte.resultado.w14 + instance.parte.llegada.w15) - (instance.parte.consumonokia.w15 + instance.parte.consumoclaro.w15)
                disponible_w16 = (instance.parte.resultado.w15 + instance.parte.llegada.w16) - (instance.parte.consumonokia.w16 + instance.parte.consumoclaro.w16)
                disponible_w17 = (instance.parte.resultado.w16 + instance.parte.llegada.w17) - (instance.parte.consumonokia.w17 + instance.parte.consumoclaro.w17)
                disponible_w18 = (instance.parte.resultado.w17 + instance.parte.llegada.w18) - (instance.parte.consumonokia.w18 + instance.parte.consumoclaro.w18)
                disponible_w19 = (instance.parte.resultado.w18 + instance.parte.llegada.w19) - (instance.parte.consumonokia.w19 + instance.parte.consumoclaro.w19)
                disponible_w20 = (instance.parte.resultado.w19 + instance.parte.llegada.w20) - (instance.parte.consumonokia.w20 + instance.parte.consumoclaro.w20)
                disponible_w21 = (instance.parte.resultado.w20 + instance.parte.llegada.w21) - (instance.parte.consumonokia.w21 + instance.parte.consumoclaro.w21)
                disponible_w22 = (instance.parte.resultado.w21 + instance.parte.llegada.w22) - (instance.parte.consumonokia.w22 + instance.parte.consumoclaro.w22)
                disponible_w23 = (instance.parte.resultado.w22 + instance.parte.llegada.w23) - (instance.parte.consumonokia.w23 + instance.parte.consumoclaro.w23)
                disponible_w24 = (instance.parte.resultado.w23 + instance.parte.llegada.w24) - (instance.parte.consumonokia.w24 + instance.parte.consumoclaro.w24)
                disponible_w25 = (instance.parte.resultado.w24 + instance.parte.llegada.w25) - (instance.parte.consumonokia.w25 + instance.parte.consumoclaro.w25)
                disponible_w26 = (instance.parte.resultado.w25 + instance.parte.llegada.w26) - (instance.parte.consumonokia.w26 + instance.parte.consumoclaro.w26)
                disponible_w27 = (instance.parte.resultado.w26 + instance.parte.llegada.w27) - (instance.parte.consumonokia.w27 + instance.parte.consumoclaro.w27)
                disponible_w28 = (instance.parte.resultado.w27 + instance.parte.llegada.w28) - (instance.parte.consumonokia.w28 + instance.parte.consumoclaro.w28)
                disponible_w29 = (instance.parte.resultado.w28 + instance.parte.llegada.w29) - (instance.parte.consumonokia.w29 + instance.parte.consumoclaro.w29)
                disponible_w30 = (instance.parte.resultado.w29 + instance.parte.llegada.w30) - (instance.parte.consumonokia.w30 + instance.parte.consumoclaro.w30)
                disponible_w31 = (instance.parte.resultado.w30 + instance.parte.llegada.w31) - (instance.parte.consumonokia.w31 + instance.parte.consumoclaro.w31)
                disponible_w32 = (instance.parte.resultado.w31 + instance.parte.llegada.w32) - (instance.parte.consumonokia.w32 + instance.parte.consumoclaro.w32)
                disponible_w33 = (instance.parte.resultado.w32 + instance.parte.llegada.w33) - (instance.parte.consumonokia.w33 + instance.parte.consumoclaro.w33)
                disponible_w34 = (instance.parte.resultado.w33 + instance.parte.llegada.w34) - (instance.parte.consumonokia.w34 + instance.parte.consumoclaro.w34)
                disponible_w35 = (instance.parte.resultado.w34 + instance.parte.llegada.w35) - (instance.parte.consumonokia.w35 + instance.parte.consumoclaro.w35)
                disponible_w36 = (instance.parte.resultado.w35 + instance.parte.llegada.w36) - (instance.parte.consumonokia.w36 + instance.parte.consumoclaro.w36)
                disponible_w37 = (instance.parte.resultado.w36 + instance.parte.llegada.w37) - (instance.parte.consumonokia.w37 + instance.parte.consumoclaro.w37)
                disponible_w38 = (instance.parte.resultado.w37 + instance.parte.llegada.w38) - (instance.parte.consumonokia.w38 + instance.parte.consumoclaro.w38)
                disponible_w39 = (instance.parte.resultado.w38 + instance.parte.llegada.w39) - (instance.parte.consumonokia.w39 + instance.parte.consumoclaro.w39)
                disponible_w40 = (instance.parte.resultado.w39 + instance.parte.llegada.w40) - (instance.parte.consumonokia.w40 + instance.parte.consumoclaro.w40)
                disponible_w41 = (instance.parte.resultado.w40 + instance.parte.llegada.w41) - (instance.parte.consumonokia.w41 + instance.parte.consumoclaro.w41)
                disponible_w42 = (instance.parte.resultado.w41 + instance.parte.llegada.w42) - (instance.parte.consumonokia.w42 + instance.parte.consumoclaro.w42)
                disponible_w43 = (instance.parte.resultado.w42 + instance.parte.llegada.w43) - (instance.parte.consumonokia.w43 + instance.parte.consumoclaro.w43)
                disponible_w44 = (instance.parte.resultado.w43 + instance.parte.llegada.w44) - (instance.parte.consumonokia.w44 + instance.parte.consumoclaro.w44)
                disponible_w45 = (instance.parte.resultado.w44 + instance.parte.llegada.w45) - (instance.parte.consumonokia.w45 + instance.parte.consumoclaro.w45)
                disponible_w46 = (instance.parte.resultado.w45 + instance.parte.llegada.w46) - (instance.parte.consumonokia.w46 + instance.parte.consumoclaro.w46)
                disponible_w47 = (instance.parte.resultado.w46 + instance.parte.llegada.w47) - (instance.parte.consumonokia.w47 + instance.parte.consumoclaro.w47)
                disponible_w48 = (instance.parte.resultado.w47 + instance.parte.llegada.w48) - (instance.parte.consumonokia.w48 + instance.parte.consumoclaro.w48)
                disponible_w49 = (instance.parte.resultado.w48 + instance.parte.llegada.w49) - (instance.parte.consumonokia.w49 + instance.parte.consumoclaro.w49)
                disponible_w50 = (instance.parte.resultado.w49 + instance.parte.llegada.w50) - (instance.parte.consumonokia.w50 + instance.parte.consumoclaro.w50)
                disponible_w51 = (instance.parte.resultado.w50 + instance.parte.llegada.w51) - (instance.parte.consumonokia.w51 + instance.parte.consumoclaro.w51)
                disponible_w52 = (instance.parte.resultado.w51 + instance.parte.llegada.w52) - (instance.parte.consumonokia.w52 + instance.parte.consumoclaro.w52)

                if disponible_w14 is not None and WEEK < 14:
                    instance.parte.disponible.w14 = disponible_w14
                if disponible_w15 is not None and WEEK < 15:
                    instance.parte.disponible.w15 = disponible_w15
                if disponible_w16 is not None and WEEK < 16:
                    instance.parte.disponible.w16 = disponible_w16
                if disponible_w17 is not None and WEEK < 17:
                    instance.parte.disponible.w17 = disponible_w17
                if disponible_w18 is not None and WEEK < 18:
                    instance.parte.disponible.w18 = disponible_w18
                if disponible_w19 is not None and WEEK < 19:
                    instance.parte.disponible.w19 = disponible_w19
                if disponible_w20 is not None and WEEK < 20:
                    instance.parte.disponible.w20 = disponible_w20
                if disponible_w21 is not None and WEEK < 21:
                    instance.parte.disponible.w21 = disponible_w21
                if disponible_w22 is not None and WEEK < 22:
                    instance.parte.disponible.w22 = disponible_w22
                if disponible_w23 is not None and WEEK < 23:
                    instance.parte.disponible.w23 = disponible_w23
                if disponible_w24 is not None and WEEK < 24:
                    instance.parte.disponible.w24 = disponible_w24
                if disponible_w25 is not None and WEEK < 25:
                    instance.parte.disponible.w25 = disponible_w25
                if disponible_w26 is not None and WEEK < 26:
                    instance.parte.disponible.w26 = disponible_w26
                if disponible_w27 is not None and WEEK < 27:
                    instance.parte.disponible.w27 = disponible_w27
                if disponible_w28 is not None and WEEK < 28:
                    instance.parte.disponible.w28 = disponible_w28
                if disponible_w29 is not None and WEEK < 29:
                    instance.parte.disponible.w29 = disponible_w29
                if disponible_w30 is not None and WEEK < 30:
                    instance.parte.disponible.w30 = disponible_w30
                if disponible_w31 is not None and WEEK < 31:
                    instance.parte.disponible.w31 = disponible_w31
                if disponible_w32 is not None and WEEK < 32:
                    instance.parte.disponible.w32 = disponible_w32
                if disponible_w33 is not None and WEEK < 33:
                    instance.parte.disponible.w33 = disponible_w33
                if disponible_w34 is not None and WEEK < 34:
                    instance.parte.disponible.w34 = disponible_w34
                if disponible_w35 is not None and WEEK < 35:
                    instance.parte.disponible.w35 = disponible_w35
                if disponible_w36 is not None and WEEK < 36:
                    instance.parte.disponible.w36 = disponible_w36
                if disponible_w37 is not None and WEEK < 37:
                    instance.parte.disponible.w37 = disponible_w37
                if disponible_w38 is not None and WEEK < 38:
                    instance.parte.disponible.w38 = disponible_w38
                if disponible_w39 is not None and WEEK < 39:
                    instance.parte.disponible.w39 = disponible_w39
                if disponible_w40 is not None and WEEK < 40:
                    instance.parte.disponible.w40 = disponible_w40
                if disponible_w41 is not None and WEEK < 41:
                    instance.parte.disponible.w41 = disponible_w41
                if disponible_w42 is not None and WEEK < 42:
                    instance.parte.disponible.w42 = disponible_w42
                if disponible_w43 is not None and WEEK < 43:
                    instance.parte.disponible.w43 = disponible_w43
                if disponible_w44 is not None and WEEK < 44:
                    instance.parte.disponible.w44 = disponible_w44
                if disponible_w45 is not None and WEEK < 45:
                    instance.parte.disponible.w45 = disponible_w45
                if disponible_w46 is not None and WEEK < 46:
                    instance.parte.disponible.w46 = disponible_w46
                if disponible_w47 is not None and WEEK < 47:
                    instance.parte.disponible.w47 = disponible_w47
                if disponible_w48 is not None and WEEK < 48:
                    instance.parte.disponible.w48 = disponible_w48
                if disponible_w49 is not None and WEEK < 49:
                    instance.parte.disponible.w49 = disponible_w49
                if disponible_w50 is not None and WEEK < 50:
                    instance.parte.disponible.w50 = disponible_w50
                if disponible_w51 is not None and WEEK < 51:
                    instance.parte.disponible.w51 = disponible_w51
                if disponible_w52 is not None and WEEK < 52:
                    instance.parte.disponible.w52 = disponible_w52

            instance.parte.disponible.save()
        except:
            pass
