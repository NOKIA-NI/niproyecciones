from django.db import models
from partes.models import Parte
from estaciones.models import Estacion
from . import choices
from estaciones import choices as estaciones_choices
from partes import choices as partes_choices
from django.db.models.signals import post_save
from django.dispatch import receiver

class AsignacionBulk(models.Model):
    parte = models.OneToOneField(Parte, on_delete=models.CASCADE, blank=True, null=True)
    cod_sap = models.PositiveIntegerField(blank=True, null=True)
    capex = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    cod_bodega = models.CharField(max_length=255, blank=True, null=True)
    bodega = models.CharField(max_length=255, blank=True, null=True)
    comentario_bodega = models.CharField(max_length=255, blank=True, null=True)
    so = models.CharField(max_length=255, default='Bulk', blank=True, null=True)
    po = models.CharField(max_length=255, default='Bulk', blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'asignacion bulk'
        verbose_name_plural = 'asignaciones bulk'

    def __str__(self):
        return self.parte.parte_nokia

    # def get_absolute_url(self):
    #     return reverse('formatos:', kwargs={'pk': self.pk})

    @receiver(post_save, sender=Parte)
    def create_asignacion_bulk(sender, instance, created, **kwargs):
        if created:
            asignacion_bulk, new = AsignacionBulk.objects.get_or_create(parte=instance,
                                                                        cod_sap=cod_sap,
                                                                        capex=capex,
                                                                        )

    @receiver(post_save, sender=Parte)
    def save_asignacion_bulk(sender, instance, **kwargs):
        instance.asignacionbulk.save()

class AsignacionAntena(models.Model):
    parte = models.OneToOneField(Parte, on_delete=models.CASCADE, blank=True, null=True)
    cod_sap = models.PositiveIntegerField(blank=True, null=True)
    capex = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    cod_bodega = models.CharField(max_length=255, blank=True, null=True)
    bodega = models.CharField(max_length=255, blank=True, null=True)
    familia = models.PositiveIntegerField(blank=True, null=True)
    caracteristicas = models.CharField(max_length=255, blank=True, null=True)
    puertos = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'asignacion antena'
        verbose_name_plural = 'asignaciones antenas'

    def __str__(self):
        return self.parte.parte_nokia

    # def get_absolute_url(self):
    #     return reverse('formatos:', kwargs={'pk': self.pk})

    @receiver(post_save, sender=Parte)
    def create_asignacion_Antena(sender, instance, created, **kwargs):
        if created:
            asignacion_Antena, new = AsignacionAntena.objects.get_or_create(parte=instance,
                                                                            cod_sap=cod_sap,
                                                                            capex=capex,
                                                                            familia=instance.grupo_numero,
                                                                            )

    @receiver(post_save, sender=Parte)
    def save_asignacion_Antena(sender, instance, **kwargs):
        instance.asignacionbulk.save()

class EstadoPo(models.Model):
    numero_po = models.PositiveIntegerField(blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='estados_po', blank=True, null=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    bts = models.PositiveIntegerField(blank=True, null=True)
    bts_status = models.CharField(max_length=255, blank=True, null=True)
    bts_arrival_week = models.PositiveIntegerField(blank=True, null=True)
    jumper = models.CharField(max_length=255, blank=True, null=True)
    jumper_status = models.CharField(max_length=255, blank=True, null=True)
    jumper_arrival_week = models.PositiveIntegerField(blank=True, null=True)
    fxcb_bts = models.CharField(max_length=255, blank=True, null=True)
    fxcb_status = models.CharField(max_length=255, blank=True, null=True)
    customs_ceared = models.DateField(blank=True, null=True)
    sr = models.CharField(max_length=255, blank=True, null=True)
    awb = models.CharField(max_length=255, blank=True, null=True)
    eta = models.DateField(blank=True, null=True)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    pre_pgi = models.CharField(max_length=255, blank=True, null=True)
    fc_impl = models.PositiveIntegerField(blank=True, null=True)
    fxcb_qty = models.PositiveIntegerField(blank=True, null=True)
    annotation = models.CharField(max_length=255, blank=True, null=True)
    comprometido = models.CharField(max_length=255, blank=True, null=True)
    share = models.CharField(max_length=255, blank=True, null=True)
    w_reviewed = models.CharField(max_length=255, blank=True, null=True)
    columna_924 = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'estado po'
        verbose_name_plural = 'estados po'

    def __str__(self):
        return self.numero_po

    # def get_absolute_url(self):
    #     return reverse('formatos:', kwargs={'pk': self.pk})
