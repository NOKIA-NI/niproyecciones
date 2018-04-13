from django.db import models

class Hwproyeccion(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    siteName = models.CharField(max_length=80, blank=True, null=True)
    proyecto = models.CharField(max_length=19, blank=True, null=True)
    escenario = models.CharField(max_length=20, blank=True, null=True)
    banda = models.CharField(max_length=30, blank=True, null=True)
    agrupadores = models.CharField(max_length=255, blank=True, null=True)
    RFE = models.DateField(blank=True, null=True)
    parte = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, default='Pendiente', blank=True, null=True)
    cantidad_estimada = models.BigIntegerField(blank=True, null=True)
    lastUpdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        # app_label = 'nokiagi'
        managed = False
        db_table = 'hw'
        verbose_name = 'hw proyeccion'
        verbose_name_plural = 'hw proyecciones'

    def __str__(self):
        return str(self.id)
