from django.db import models

class HwProyeccion(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    siteName = models.CharField(max_length=80, blank=True, null=True)
    proyecto = models.CharField(max_length=19, blank=True, null=True)
    escenario = models.CharField(max_length=20, blank=True, null=True)
    banda = models.CharField(max_length=30, blank=True, null=True)
    agrupadores = models.CharField(max_length=255, blank=True, null=True)
    rfe = models.DateField(blank=True, null=True)
    parte = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, default='Pendiente', blank=True, null=True)
    cantidad_estimada = models.BigIntegerField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hw'
        verbose_name = 'hw proyeccion'
        verbose_name_plural = 'hw proyecciones'

    def __str__(self):
        return str(self.id)

class HwEstacion(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    siteName = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    scope_claro = models.CharField(max_length=150, blank=True, null=True)
    proyeccion_instalacion = models.DateField(blank=True, null=True)
    w_proyeccion_instalacion = models.IntegerField(blank=True, null=True)
    actividades = models.BigIntegerField(default=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estaciones'
        verbose_name = 'hw estacion'
        verbose_name_plural = 'hw estaciones'

    def __str__(self):
        return str(self.id)

class HwParte(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    cod_capex = models.CharField(max_length=255, blank=True, null=True)
    nombre_nokia = models.CharField(max_length=45, blank=True, null=True)
    nombre_capex = models.CharField(max_length=255, blank=True, null=True)
    seccion_parte = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partes'
        verbose_name = 'hw parte'
        verbose_name_plural = 'hw partes'

    def __str__(self):
        return str(self.id)
