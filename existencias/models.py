from django.db import models

from django.urls import reverse
from partes import choices
from partes.models import Parte
from django.db.models.signals import post_save
from django.dispatch import receiver
from consumos.models import ConsumoNokia, ConsumoClaro
from llegadas.models import Llegada
from django.utils import timezone

TODAY = timezone.now()
WEEK = TODAY.isocalendar()[1]

class Existencia(models.Model):
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
        verbose_name = 'existencia'
        verbose_name_plural = 'existencias'

    def __str__(self):
        return self.parte.parte_nokia

    def get_absolute_url(self):
        return reverse('existencias:detail_existencia', kwargs={'pk': self.pk})

    @receiver(post_save, sender=Parte)
    def create_existencia(sender, instance, created, **kwargs):
        if created:
            existencia, new = Existencia.objects.get_or_create(parte=instance,
                                                               grupo_parte=instance.grupo_parte)

    @receiver(post_save, sender=Parte)
    def save_existencia(sender, instance, **kwargs):
        instance.existencia.grupo_parte = instance.grupo_parte
        instance.existencia.save()

    @receiver(post_save, sender=ConsumoNokia)
    @receiver(post_save, sender=ConsumoClaro)
    @receiver(post_save, sender=Llegada)
    def calculate_existencia(sender, instance, **kwargs):
        try:
            if instance.parte and instance.parte.consumonokia and instance.parte.consumoclaro and instance.parte.llegada and instance.parte.existencia:
                existencia_w14 = instance.parte.resultado.w14
                existencia_w15 = instance.parte.resultado.w14
                existencia_w16 = instance.parte.resultado.w15
                existencia_w17 = instance.parte.resultado.w16
                existencia_w18 = instance.parte.resultado.w17
                existencia_w19 = instance.parte.resultado.w18
                existencia_w20 = instance.parte.resultado.w19
                existencia_w21 = instance.parte.resultado.w20
                existencia_w22 = instance.parte.resultado.w21
                existencia_w23 = instance.parte.resultado.w22
                existencia_w24 = instance.parte.resultado.w23
                existencia_w25 = instance.parte.resultado.w24
                existencia_w26 = instance.parte.resultado.w25
                existencia_w27 = instance.parte.resultado.w26
                existencia_w28 = instance.parte.resultado.w27
                existencia_w29 = instance.parte.resultado.w28
                existencia_w30 = instance.parte.resultado.w29
                existencia_w31 = instance.parte.resultado.w30
                existencia_w32 = instance.parte.resultado.w31
                existencia_w33 = instance.parte.resultado.w32
                existencia_w34 = instance.parte.resultado.w33
                existencia_w35 = instance.parte.resultado.w34
                existencia_w36 = instance.parte.resultado.w35
                existencia_w37 = instance.parte.resultado.w36
                existencia_w38 = instance.parte.resultado.w37
                existencia_w39 = instance.parte.resultado.w38
                existencia_w40 = instance.parte.resultado.w39
                existencia_w41 = instance.parte.resultado.w40
                existencia_w42 = instance.parte.resultado.w41
                existencia_w43 = instance.parte.resultado.w42
                existencia_w44 = instance.parte.resultado.w43
                existencia_w45 = instance.parte.resultado.w44
                existencia_w46 = instance.parte.resultado.w45
                existencia_w47 = instance.parte.resultado.w46
                existencia_w48 = instance.parte.resultado.w47
                existencia_w49 = instance.parte.resultado.w48
                existencia_w50 = instance.parte.resultado.w49
                existencia_w51 = instance.parte.resultado.w50
                existencia_w52 = instance.parte.resultado.w51

                if existencia_w14 is not None and WEEK < 14:
                    instance.parte.existencia.w14 = existencia_w14
                if existencia_w15 is not None and WEEK < 15:
                    instance.parte.existencia.w15 = existencia_w15
                if existencia_w16 is not None and WEEK < 16:
                    instance.parte.existencia.w16 = existencia_w16
                if existencia_w17 is not None and WEEK < 17:
                    instance.parte.existencia.w17 = existencia_w17
                if existencia_w18 is not None and WEEK < 18:
                    instance.parte.existencia.w18 = existencia_w18
                if existencia_w19 is not None and WEEK < 19:
                    instance.parte.existencia.w19 = existencia_w19
                if existencia_w20 is not None and WEEK < 20:
                    instance.parte.existencia.w20 = existencia_w20
                if existencia_w21 is not None and WEEK < 21:
                    instance.parte.existencia.w21 = existencia_w21
                if existencia_w22 is not None and WEEK < 22:
                    instance.parte.existencia.w22 = existencia_w22
                if existencia_w23 is not None and WEEK < 23:
                    instance.parte.existencia.w23 = existencia_w23
                if existencia_w24 is not None and WEEK < 24:
                    instance.parte.existencia.w24 = existencia_w24
                if existencia_w25 is not None and WEEK < 25:
                    instance.parte.existencia.w25 = existencia_w25
                if existencia_w26 is not None and WEEK < 26:
                    instance.parte.existencia.w26 = existencia_w26
                if existencia_w27 is not None and WEEK < 27:
                    instance.parte.existencia.w27 = existencia_w27
                if existencia_w28 is not None and WEEK < 28:
                    instance.parte.existencia.w28 = existencia_w28
                if existencia_w29 is not None and WEEK < 29:
                    instance.parte.existencia.w29 = existencia_w29
                if existencia_w30 is not None and WEEK < 30:
                    instance.parte.existencia.w30 = existencia_w30
                if existencia_w31 is not None and WEEK < 31:
                    instance.parte.existencia.w31 = existencia_w31
                if existencia_w32 is not None and WEEK < 32:
                    instance.parte.existencia.w32 = existencia_w32
                if existencia_w33 is not None and WEEK < 33:
                    instance.parte.existencia.w33 = existencia_w33
                if existencia_w34 is not None and WEEK < 34:
                    instance.parte.existencia.w34 = existencia_w34
                if existencia_w35 is not None and WEEK < 35:
                    instance.parte.existencia.w35 = existencia_w35
                if existencia_w36 is not None and WEEK < 36:
                    instance.parte.existencia.w36 = existencia_w36
                if existencia_w37 is not None and WEEK < 37:
                    instance.parte.existencia.w37 = existencia_w37
                if existencia_w38 is not None and WEEK < 38:
                    instance.parte.existencia.w38 = existencia_w38
                if existencia_w39 is not None and WEEK < 39:
                    instance.parte.existencia.w39 = existencia_w39
                if existencia_w40 is not None and WEEK < 40:
                    instance.parte.existencia.w40 = existencia_w40
                if existencia_w41 is not None and WEEK < 41:
                    instance.parte.existencia.w41 = existencia_w41
                if existencia_w42 is not None and WEEK < 42:
                    instance.parte.existencia.w42 = existencia_w42
                if existencia_w43 is not None and WEEK < 43:
                    instance.parte.existencia.w43 = existencia_w43
                if existencia_w44 is not None and WEEK < 44:
                    instance.parte.existencia.w44 = existencia_w44
                if existencia_w45 is not None and WEEK < 45:
                    instance.parte.existencia.w45 = existencia_w45
                if existencia_w46 is not None and WEEK < 46:
                    instance.parte.existencia.w46 = existencia_w46
                if existencia_w47 is not None and WEEK < 47:
                    instance.parte.existencia.w47 = existencia_w47
                if existencia_w48 is not None and WEEK < 48:
                    instance.parte.existencia.w48 = existencia_w48
                if existencia_w49 is not None and WEEK < 49:
                    instance.parte.existencia.w49 = existencia_w49
                if existencia_w50 is not None and WEEK < 50:
                    instance.parte.existencia.w50 = existencia_w50
                if existencia_w51 is not None and WEEK < 51:
                    instance.parte.existencia.w51 = existencia_w51
                if existencia_w52 is not None and WEEK < 52:
                    instance.parte.existencia.w52 = existencia_w52

            instance.parte.existencia.save()
        except:
            pass
