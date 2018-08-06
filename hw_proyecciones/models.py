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
    ciudad = models.CharField(max_length=40, blank=True, null=True)
    scope_claro = models.CharField(max_length=150, blank=True, null=True)
    proyeccion_instalacion = models.DateField(blank=True, null=True)
    w_proyeccion_instalacion = models.IntegerField(blank=True, null=True)
    actividades = models.BigIntegerField(blank=True, null=True)
    bolsa = models.CharField(max_length=255, blank=True, null=True)
    w_fc_c = models.CharField(max_length=45, blank=True, null=True)
    status_nokia = models.CharField(max_length=255, blank=True, null=True)

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

class HwSiteList(models.Model):
    idsitesList = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    siteName = models.CharField(max_length=100, blank=True, null=True)
    zona = models.CharField(max_length=20, blank=True, null=True)
    proyeccion_instalacion = models.DateField(blank=True, null=True)
    W_Proyeccion_Instalacion = models.PositiveIntegerField(blank=True, null=True)
    scope_claro = models.CharField(max_length=150, blank=True, null=True)
    Bolsa_HW = models.CharField(max_length=255, blank=True, null=True)
    w_fc_c = models.PositiveIntegerField(blank=True, null=True)
    status_nokia = models.CharField(max_length=255, blank=True, null=True)
    estado_HW = models.CharField(max_length=13, blank=True, null=True)
    fecha_solicitud_hw = models.DateField(blank=True, null=True)
    solicitante_asignacion_hw = models.BigIntegerField(blank=True, null=True)
    solicitud_hw = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sitesList_hw'
        verbose_name = 'hw sitelist'
        verbose_name_plural = 'hw sitelist'

    def __str__(self):
        return str(self.idsitesList)

class HwControlRfe(models.Model):
    id_hw_config = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    wp = models.BigIntegerField(blank=True, null=True)
    siteName = models.CharField(max_length=60, blank=True, null=True)
    proyecto = models.CharField(max_length=30, blank=True, null=True)
    escenario = models.CharField(max_length=20, blank=True, null=True)
    banda = models.CharField(max_length=30, blank=True, null=True)
    seccion = models.CharField(max_length=45, blank=True, null=True)
    referencia = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    parte = models.CharField(max_length=45, blank=True, null=True)
    total_smr = models.BigIntegerField(blank=True, null=True)
    fuente = models.CharField(max_length=45, blank=True, null=True)
    RFE = models.DateField(blank=True, null=True)
    so = models.CharField(max_length=255, blank=True, null=True)# si
    po = models.CharField(max_length=255, blank=True, null=True)# si
    bodega_origen = models.CharField(max_length=50, blank=True, null=True)# si
    bodega_origen_fecha = models.DateField(blank=True, null=True)
    issue_bodega_origen = models.CharField(max_length=255, blank=True, null=True)# si
    material_sobrante = models.TextField(blank=True, null=True)# si
    bts_status = models.CharField(max_length=50, blank=True, null=True)
    reemplazo = models.CharField(max_length=255, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    so_date = models.DateField(blank=True, null=True)
    envio_capex = models.DateField(blank=True, null=True)
    last_updated_ghw = models.DateField(blank=True, null=True)
    homologacion = models.CharField(max_length=85, blank=True, null=True)# si
    

    class Meta:
        managed = False
        db_table = 'hw_control_rfe'
        verbose_name = 'hw control rfe'
        verbose_name_plural = 'hw control rfe'

    def __str__(self):
        return str(self.id_hw_config)
    
    def save(self, *args, **kwargs):
        super(HwControlRfe, self).save(update_fields=['so', 'po', 'bodega_origen', 'issue_bodega_origen', 'material_sobrante', 'homologacion'], *args, **kwargs)