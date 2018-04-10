from django.db import models

from django.urls import reverse
from partes import choices
from partes.models import Parte
from django.db.models.signals import post_save
from django.dispatch import receiver

class Llegada(models.Model):
    parte = models.OneToOneField(Parte, on_delete=models.CASCADE)
    grupo_parte = models.CharField(max_length=255, choices=choices.GRUPO_PARTE_CHOICES, blank=True, null=True)
    w14 = models.PositiveIntegerField(blank=True, null=True)
    w15 = models.PositiveIntegerField(blank=True, null=True)
    w16 = models.PositiveIntegerField(blank=True, null=True)
    w17 = models.PositiveIntegerField(blank=True, null=True)
    w18 = models.PositiveIntegerField(blank=True, null=True)
    w19 = models.PositiveIntegerField(blank=True, null=True)
    w20 = models.PositiveIntegerField(blank=True, null=True)
    w21 = models.PositiveIntegerField(blank=True, null=True)
    w22 = models.PositiveIntegerField(blank=True, null=True)
    w23 = models.PositiveIntegerField(blank=True, null=True)
    w24 = models.PositiveIntegerField(blank=True, null=True)
    w25 = models.PositiveIntegerField(blank=True, null=True)
    w26 = models.PositiveIntegerField(blank=True, null=True)
    w27 = models.PositiveIntegerField(blank=True, null=True)
    w28 = models.PositiveIntegerField(blank=True, null=True)
    w29 = models.PositiveIntegerField(blank=True, null=True)
    w30 = models.PositiveIntegerField(blank=True, null=True)
    w31 = models.PositiveIntegerField(blank=True, null=True)
    w32 = models.PositiveIntegerField(blank=True, null=True)
    w33 = models.PositiveIntegerField(blank=True, null=True)
    w34 = models.PositiveIntegerField(blank=True, null=True)
    w35 = models.PositiveIntegerField(blank=True, null=True)
    w36 = models.PositiveIntegerField(blank=True, null=True)
    w37 = models.PositiveIntegerField(blank=True, null=True)
    w38 = models.PositiveIntegerField(blank=True, null=True)
    w39 = models.PositiveIntegerField(blank=True, null=True)
    w40 = models.PositiveIntegerField(blank=True, null=True)
    w41 = models.PositiveIntegerField(blank=True, null=True)
    w42 = models.PositiveIntegerField(blank=True, null=True)
    w43 = models.PositiveIntegerField(blank=True, null=True)
    w44 = models.PositiveIntegerField(blank=True, null=True)
    w45 = models.PositiveIntegerField(blank=True, null=True)
    w46 = models.PositiveIntegerField(blank=True, null=True)
    w47 = models.PositiveIntegerField(blank=True, null=True)
    w48 = models.PositiveIntegerField(blank=True, null=True)
    w49 = models.PositiveIntegerField(blank=True, null=True)
    w50 = models.PositiveIntegerField(blank=True, null=True)
    w51 = models.PositiveIntegerField(blank=True, null=True)
    w52 = models.PositiveIntegerField(blank=True, null=True)

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
