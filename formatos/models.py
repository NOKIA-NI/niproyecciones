from django.db import models
from estaciones.models import Estacion
from partes.models import Parte
from . import choices
from estaciones import choices as estaciones_choices
from partes import choices as partes_choices
from django.db.models.signals import post_save
from django.dispatch import receiver

ENERO = [1, 2, 3, 4, 5]
FEBRERO = [6, 7, 8, 9]
MARZO = [10, 11, 12, 13]
ABRIL = [14, 15, 16, 17]
MAYO = [18, 19, 20, 21, 22]
JUNIO = [23, 24, 25, 26]
JULIO = [27, 28, 29, 30]
AGOSTO = [31, 32, 33, 34, 35]
SEPTIEMBRE = [36, 37, 38, 39]
OCTUBRE = [40, 41, 42, 43, 44]
NOVIEMBRE = [45, 46, 47, 48]
DICIEMBRE = [49, 50, 51, 52]


class FormatoEstacion(models.Model):
    estacion = models.OneToOneField(Estacion, on_delete=models.CASCADE, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'formato estacion'
        verbose_name_plural = 'formatos estacion'

    def __str__(self):
        return self.estacion.site_name

    # def get_absolute_url(self):
    #     return reverse('formatos:detail_estacion', kwargs={'pk': self.pk})

class FormatoParte(models.Model):
    formato_estacion = models.ForeignKey(FormatoEstacion, on_delete=models.CASCADE, related_name='formatos_parte', blank=True, null=True)
    parte = models.ForeignKey(Parte, on_delete=models.CASCADE, related_name='formatos_parte', blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'formato parte'
        verbose_name_plural = 'formatos parte'
        unique_together = ('formato_estacion', 'parte')

    def __str__(self):
        return self.parte.parte_nokia

    # def get_absolute_url(self):
    #     return reverse('formatos:detail_estacion', kwargs={'pk': self.pk})


class FormatoClaro(models.Model):
    # formato_parte = models.ForeignKey(FormatoParte, on_delete=models.CASCADE, related_name='formatos_claro', blank=True, null=True)
    formato_parte = models.OneToOneField(FormatoParte, on_delete=models.CASCADE, blank=True, null=True)
    id_sitio = models.CharField(max_length=255, blank=True, null=True)
    sitio = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='formatos_claro', blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)
    sap = models.PositiveIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    regional = models.CharField(max_length=255, choices=estaciones_choices.REGION_CHOICES, blank=True, null=True)
    semana = models.PositiveIntegerField(blank=True, null=True)
    mes = models.CharField(max_length=255, choices=choices.MES_CHOICES, blank=True, null=True)
    generado = models.DateField(auto_now_add=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'formato claro'
        verbose_name_plural = 'formatos claro'

    def __str__(self):
        return self.formato_parte.formato_estacion.estacion.site_name

    # def get_absolute_url(self):
    #     return reverse('formatos:detail_estacion', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        
        self.sitio = self.formato_parte.formato_estacion.estacion
        self.sap = self.formato_parte.parte.cod_sap
        self.descripcion = self.formato_parte.parte.capex
        self.qty = self.formato_parte.cantidad
        self.ciudad = self.formato_parte.formato_estacion.estacion.ciudad
        self.regional = self.formato_parte.formato_estacion.estacion.region
        self.semana = self.formato_parte.formato_estacion.estacion.w_fc_sal

        if self.semana in ENERO:
            MONTH = 'Enero'
        if self.semana in FEBRERO:
            MONTH = 'Febrero'
        if self.semana in MARZO:
            MONTH = 'Marzo'
        if self.semana in ABRIL:
            MONTH = 'Abril'
        if self.semana in MAYO:
            MONTH = 'Mayo'
        if self.semana in JUNIO:
            MONTH = 'Junio'
        if self.semana in JULIO:
            MONTH = 'Julio'
        if self.semana in AGOSTO:
            MONTH = 'Agosto'
        if self.semana in SEPTIEMBRE:
            MONTH = 'Septiembre'
        if self.semana in OCTUBRE:
            MONTH = 'Octubre'
        if self.semana in NOVIEMBRE:
            MONTH = 'Noviembre'
        if self.semana in DICIEMBRE:
            MONTH = 'Diciembre'
        self.mes = MONTH
        
        super(FormatoClaro, self).save(*args, **kwargs)

    @receiver(post_save, sender=FormatoParte)
    def create_formato_claro(sender, instance, created, **kwargs):
        if created:
            formato_claro, new = FormatoClaro.objects.get_or_create(formato_parte=instance,)

    @receiver(post_save, sender=FormatoParte)
    def save_formato_claro(sender, instance, **kwargs):
        instance.formatoclaro.save()

class FormatoClaroTotal(models.Model):
    parte = models.OneToOneField(Parte, on_delete=models.CASCADE, blank=True, null=True)
    cod_sap = models.PositiveIntegerField(blank=True, null=True)
    capex = models.CharField(max_length=255, blank=True, null=True)
    grupo_parte = models.CharField(max_length=255, choices=partes_choices.GRUPO_PARTE_CHOICES, blank=True, null=True)
    total = models.PositiveIntegerField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'formato claro total'
        verbose_name_plural = 'formatos claro total'

    def __str__(self):
        return self.parte.parte_nokia

    # def get_absolute_url(self):
    #     return reverse('formatos:detail_estacion', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        
        self.cod_sap = self.parte.cod_sap
        self.capex = self.parte.capex
        self.grupo_parte = self.parte.grupo_parte
        
        super(FormatoClaroTotal, self).save(*args, **kwargs)
