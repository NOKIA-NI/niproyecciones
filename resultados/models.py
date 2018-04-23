from django.db import models

from django.urls import reverse
from partes import choices
from partes.models import Parte
from django.db.models.signals import post_save
from django.dispatch import receiver
from consumos.models import ConsumoNokia, ConsumoClaro
from llegadas.models import Llegada
from existencias.models import Existencia

class Resultado(models.Model):
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
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'

    def __str__(self):
        return self.parte.parte_nokia

    def get_absolute_url(self):
        return reverse('resultados:detail_resultado', kwargs={'pk': self.pk})

    @receiver(post_save, sender=Parte)
    def create_resultado(sender, instance, created, **kwargs):
        if created:
            resultado, new = Resultado.objects.get_or_create(parte=instance,
                                                         grupo_parte=instance.grupo_parte)

    @receiver(post_save, sender=Parte)
    def save_resultado(sender, instance, **kwargs):
        instance.resultado.grupo_parte = instance.grupo_parte
        instance.resultado.save()

    @receiver(post_save, sender=ConsumoNokia)
    @receiver(post_save, sender=ConsumoClaro)
    @receiver(post_save, sender=Llegada)
    @receiver(post_save, sender=Existencia)
    def calculate_resultado(sender, instance, **kwargs):
        try:
            if instance.parte and instance.parte.consumonokia and instance.parte.consumoclaro and instance.parte.llegada and instance.parte.existencia:
                resultado_w14 = (instance.parte.existencia.w14 + instance.parte.llegada.w14) - (instance.parte.consumonokia.w14 + instance.parte.consumoclaro.w14)
                resultado_w15 = (instance.parte.existencia.w15 + instance.parte.llegada.w15) - (instance.parte.consumonokia.w15 + instance.parte.consumoclaro.w15)
                resultado_w16 = (instance.parte.existencia.w16 + instance.parte.llegada.w16) - (instance.parte.consumonokia.w16 + instance.parte.consumoclaro.w16)
                resultado_w17 = (instance.parte.existencia.w17 + instance.parte.llegada.w17) - (instance.parte.consumonokia.w17 + instance.parte.consumoclaro.w17)
                resultado_w18 = (instance.parte.existencia.w18 + instance.parte.llegada.w18) - (instance.parte.consumonokia.w18 + instance.parte.consumoclaro.w18)
                resultado_w19 = (instance.parte.existencia.w19 + instance.parte.llegada.w19) - (instance.parte.consumonokia.w19 + instance.parte.consumoclaro.w19)
                resultado_w20 = (instance.parte.existencia.w20 + instance.parte.llegada.w20) - (instance.parte.consumonokia.w20 + instance.parte.consumoclaro.w20)
                resultado_w21 = (instance.parte.existencia.w21 + instance.parte.llegada.w21) - (instance.parte.consumonokia.w21 + instance.parte.consumoclaro.w21)
                resultado_w22 = (instance.parte.existencia.w22 + instance.parte.llegada.w22) - (instance.parte.consumonokia.w22 + instance.parte.consumoclaro.w22)
                resultado_w23 = (instance.parte.existencia.w23 + instance.parte.llegada.w23) - (instance.parte.consumonokia.w23 + instance.parte.consumoclaro.w23)
                resultado_w24 = (instance.parte.existencia.w24 + instance.parte.llegada.w24) - (instance.parte.consumonokia.w24 + instance.parte.consumoclaro.w24)
                resultado_w25 = (instance.parte.existencia.w25 + instance.parte.llegada.w25) - (instance.parte.consumonokia.w25 + instance.parte.consumoclaro.w25)
                resultado_w26 = (instance.parte.existencia.w26 + instance.parte.llegada.w26) - (instance.parte.consumonokia.w26 + instance.parte.consumoclaro.w26)
                resultado_w27 = (instance.parte.existencia.w27 + instance.parte.llegada.w27) - (instance.parte.consumonokia.w27 + instance.parte.consumoclaro.w27)
                resultado_w28 = (instance.parte.existencia.w28 + instance.parte.llegada.w28) - (instance.parte.consumonokia.w28 + instance.parte.consumoclaro.w28)
                resultado_w29 = (instance.parte.existencia.w29 + instance.parte.llegada.w29) - (instance.parte.consumonokia.w29 + instance.parte.consumoclaro.w29)
                resultado_w30 = (instance.parte.existencia.w30 + instance.parte.llegada.w30) - (instance.parte.consumonokia.w30 + instance.parte.consumoclaro.w30)
                resultado_w31 = (instance.parte.existencia.w31 + instance.parte.llegada.w31) - (instance.parte.consumonokia.w31 + instance.parte.consumoclaro.w31)
                resultado_w32 = (instance.parte.existencia.w32 + instance.parte.llegada.w32) - (instance.parte.consumonokia.w32 + instance.parte.consumoclaro.w32)
                resultado_w33 = (instance.parte.existencia.w33 + instance.parte.llegada.w33) - (instance.parte.consumonokia.w33 + instance.parte.consumoclaro.w33)
                resultado_w34 = (instance.parte.existencia.w34 + instance.parte.llegada.w34) - (instance.parte.consumonokia.w34 + instance.parte.consumoclaro.w34)
                resultado_w35 = (instance.parte.existencia.w35 + instance.parte.llegada.w35) - (instance.parte.consumonokia.w35 + instance.parte.consumoclaro.w35)
                resultado_w36 = (instance.parte.existencia.w36 + instance.parte.llegada.w36) - (instance.parte.consumonokia.w36 + instance.parte.consumoclaro.w36)
                resultado_w37 = (instance.parte.existencia.w37 + instance.parte.llegada.w37) - (instance.parte.consumonokia.w37 + instance.parte.consumoclaro.w37)
                resultado_w38 = (instance.parte.existencia.w38 + instance.parte.llegada.w38) - (instance.parte.consumonokia.w38 + instance.parte.consumoclaro.w38)
                resultado_w39 = (instance.parte.existencia.w39 + instance.parte.llegada.w39) - (instance.parte.consumonokia.w39 + instance.parte.consumoclaro.w39)
                resultado_w40 = (instance.parte.existencia.w40 + instance.parte.llegada.w40) - (instance.parte.consumonokia.w40 + instance.parte.consumoclaro.w40)
                resultado_w41 = (instance.parte.existencia.w41 + instance.parte.llegada.w41) - (instance.parte.consumonokia.w41 + instance.parte.consumoclaro.w41)
                resultado_w42 = (instance.parte.existencia.w42 + instance.parte.llegada.w42) - (instance.parte.consumonokia.w42 + instance.parte.consumoclaro.w42)
                resultado_w43 = (instance.parte.existencia.w43 + instance.parte.llegada.w43) - (instance.parte.consumonokia.w43 + instance.parte.consumoclaro.w43)
                resultado_w44 = (instance.parte.existencia.w44 + instance.parte.llegada.w44) - (instance.parte.consumonokia.w44 + instance.parte.consumoclaro.w44)
                resultado_w45 = (instance.parte.existencia.w45 + instance.parte.llegada.w45) - (instance.parte.consumonokia.w45 + instance.parte.consumoclaro.w45)
                resultado_w46 = (instance.parte.existencia.w46 + instance.parte.llegada.w46) - (instance.parte.consumonokia.w46 + instance.parte.consumoclaro.w46)
                resultado_w47 = (instance.parte.existencia.w47 + instance.parte.llegada.w47) - (instance.parte.consumonokia.w47 + instance.parte.consumoclaro.w47)
                resultado_w48 = (instance.parte.existencia.w48 + instance.parte.llegada.w48) - (instance.parte.consumonokia.w48 + instance.parte.consumoclaro.w48)
                resultado_w49 = (instance.parte.existencia.w49 + instance.parte.llegada.w49) - (instance.parte.consumonokia.w49 + instance.parte.consumoclaro.w49)
                resultado_w50 = (instance.parte.existencia.w50 + instance.parte.llegada.w50) - (instance.parte.consumonokia.w50 + instance.parte.consumoclaro.w50)
                resultado_w51 = (instance.parte.existencia.w51 + instance.parte.llegada.w51) - (instance.parte.consumonokia.w51 + instance.parte.consumoclaro.w51)
                resultado_w52 = (instance.parte.existencia.w52 + instance.parte.llegada.w52) - (instance.parte.consumonokia.w52 + instance.parte.consumoclaro.w52)

                if resultado_w14 is not None:
                    instance.parte.resultado.w14 = resultado_w14
                if resultado_w15 is not None:
                    instance.parte.resultado.w15 = resultado_w15
                if resultado_w16 is not None:
                    instance.parte.resultado.w16 = resultado_w16
                if resultado_w17 is not None:
                    instance.parte.resultado.w17 = resultado_w17
                if resultado_w18 is not None:
                    instance.parte.resultado.w18 = resultado_w18
                if resultado_w19 is not None:
                    instance.parte.resultado.w19 = resultado_w19
                if resultado_w20 is not None:
                    instance.parte.resultado.w20 = resultado_w20
                if resultado_w21 is not None:
                    instance.parte.resultado.w21 = resultado_w21
                if resultado_w22 is not None:
                    instance.parte.resultado.w22 = resultado_w22
                if resultado_w23 is not None:
                    instance.parte.resultado.w23 = resultado_w23
                if resultado_w24 is not None:
                    instance.parte.resultado.w24 = resultado_w24
                if resultado_w25 is not None:
                    instance.parte.resultado.w25 = resultado_w25
                if resultado_w26 is not None:
                    instance.parte.resultado.w26 = resultado_w26
                if resultado_w27 is not None:
                    instance.parte.resultado.w27 = resultado_w27
                if resultado_w28 is not None:
                    instance.parte.resultado.w28 = resultado_w28
                if resultado_w29 is not None:
                    instance.parte.resultado.w29 = resultado_w29
                if resultado_w30 is not None:
                    instance.parte.resultado.w30 = resultado_w30
                if resultado_w31 is not None:
                    instance.parte.resultado.w31 = resultado_w31
                if resultado_w32 is not None:
                    instance.parte.resultado.w32 = resultado_w32
                if resultado_w33 is not None:
                    instance.parte.resultado.w33 = resultado_w33
                if resultado_w34 is not None:
                    instance.parte.resultado.w34 = resultado_w34
                if resultado_w35 is not None:
                    instance.parte.resultado.w35 = resultado_w35
                if resultado_w36 is not None:
                    instance.parte.resultado.w36 = resultado_w36
                if resultado_w37 is not None:
                    instance.parte.resultado.w37 = resultado_w37
                if resultado_w38 is not None:
                    instance.parte.resultado.w38 = resultado_w38
                if resultado_w39 is not None:
                    instance.parte.resultado.w39 = resultado_w39
                if resultado_w40 is not None:
                    instance.parte.resultado.w40 = resultado_w40
                if resultado_w41 is not None:
                    instance.parte.resultado.w41 = resultado_w41
                if resultado_w42 is not None:
                    instance.parte.resultado.w42 = resultado_w42
                if resultado_w43 is not None:
                    instance.parte.resultado.w43 = resultado_w43
                if resultado_w44 is not None:
                    instance.parte.resultado.w44 = resultado_w44
                if resultado_w45 is not None:
                    instance.parte.resultado.w45 = resultado_w45
                if resultado_w46 is not None:
                    instance.parte.resultado.w46 = resultado_w46
                if resultado_w47 is not None:
                    instance.parte.resultado.w47 = resultado_w47
                if resultado_w48 is not None:
                    instance.parte.resultado.w48 = resultado_w48
                if resultado_w49 is not None:
                    instance.parte.resultado.w49 = resultado_w49
                if resultado_w50 is not None:
                    instance.parte.resultado.w50 = resultado_w50
                if resultado_w51 is not None:
                    instance.parte.resultado.w51 = resultado_w51
                if resultado_w52 is not None:
                    instance.parte.resultado.w52 = resultado_w52

            instance.parte.resultado.save()
        except:
            pass
