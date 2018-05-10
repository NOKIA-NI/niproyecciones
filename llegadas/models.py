from django.db import models

from django.urls import reverse
from partes import choices
from partes.models import Parte
from django.db.models.signals import post_save
from django.dispatch import receiver

class Llegada(models.Model):
    parte = models.OneToOneField(Parte, on_delete=models.CASCADE, blank=True, null=True)
    grupo_parte = models.CharField(max_length=255, choices=choices.GRUPO_PARTE_CHOICES, blank=True, null=True)
    w14 = models.PositiveIntegerField(default=0)
    w15 = models.PositiveIntegerField(default=0)
    w16 = models.PositiveIntegerField(default=0)
    w17 = models.PositiveIntegerField(default=0)
    w18 = models.PositiveIntegerField(default=0)
    w19 = models.PositiveIntegerField(default=0)
    w20 = models.PositiveIntegerField(default=0)
    w21 = models.PositiveIntegerField(default=0)
    w22 = models.PositiveIntegerField(default=0)
    w23 = models.PositiveIntegerField(default=0)
    w24 = models.PositiveIntegerField(default=0)
    w25 = models.PositiveIntegerField(default=0)
    w26 = models.PositiveIntegerField(default=0)
    w27 = models.PositiveIntegerField(default=0)
    w28 = models.PositiveIntegerField(default=0)
    w29 = models.PositiveIntegerField(default=0)
    w30 = models.PositiveIntegerField(default=0)
    w31 = models.PositiveIntegerField(default=0)
    w32 = models.PositiveIntegerField(default=0)
    w33 = models.PositiveIntegerField(default=0)
    w34 = models.PositiveIntegerField(default=0)
    w35 = models.PositiveIntegerField(default=0)
    w36 = models.PositiveIntegerField(default=0)
    w37 = models.PositiveIntegerField(default=0)
    w38 = models.PositiveIntegerField(default=0)
    w39 = models.PositiveIntegerField(default=0)
    w40 = models.PositiveIntegerField(default=0)
    w41 = models.PositiveIntegerField(default=0)
    w42 = models.PositiveIntegerField(default=0)
    w43 = models.PositiveIntegerField(default=0)
    w44 = models.PositiveIntegerField(default=0)
    w45 = models.PositiveIntegerField(default=0)
    w46 = models.PositiveIntegerField(default=0)
    w47 = models.PositiveIntegerField(default=0)
    w48 = models.PositiveIntegerField(default=0)
    w49 = models.PositiveIntegerField(default=0)
    w50 = models.PositiveIntegerField(default=0)
    w51 = models.PositiveIntegerField(default=0)
    w52 = models.PositiveIntegerField(default=0)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'llegada'
        verbose_name_plural = 'llegadas'

    def __str__(self):
        return self.parte.parte_nokia

    def get_absolute_url(self):
        return reverse('llegadas:detail_llegada', kwargs={'pk': self.pk})

    @receiver(post_save, sender=Parte)
    def create_llegada(sender, instance, created, **kwargs):
        if created:
            llegada, new = Llegada.objects.get_or_create(parte=instance,
                                                         grupo_parte=instance.grupo_parte)

    @receiver(post_save, sender=Parte)
    def save_llegada(sender, instance, **kwargs):
        instance.llegada.grupo_parte = instance.grupo_parte
        instance.llegada.save()
