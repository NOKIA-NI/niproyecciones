""" REGION_CHOICES  """
CENTRO = 'Centro'
COSTA = 'Costa'
ORIENTE = 'Oriente'
OCCIDENTE = 'Occidente'
NOR_ORIENTE = 'Nor Oriente'
NOR_OCCIDENTE = 'Nor Occidente'
SUR_ORIENTE = 'Sur Oriente'
SUR_OCCIDENTE = 'Sur Occidente'
REGION_CHOICES = (
    ('', '---------'),
    (CENTRO, 'Centro'),
    (COSTA, 'Costa'),
    (ORIENTE, 'Oriente'),
    (OCCIDENTE, 'Occidente'),
    (NOR_ORIENTE, 'Nor Oriente'),
    (NOR_OCCIDENTE, 'Nor Occidente'),
    (SUR_ORIENTE, 'Sur Oriente'),
    (SUR_OCCIDENTE, 'Sur Occidente'),
)

""" SCOPE_CHOICES  """
SCOPE_CHOICES = (
    ('[MP2018]', '[MP2018]'),
    ('[MP2018][Integrado_2017]', '[MP2018][Integrado_2017]'),
)

""" ESTADO_WR_CHOICES  """
ESTADO_WR_CHOICES = (
    ('Integrado', 'Integrado'),
    ('On_Air', 'On_Air'),
    ('Solicitud_Abastecimiento', 'Solicitud_Abastecimiento'),
    ('Instalado', 'Instalado'),
    ('Solicitud_Partes_Capex', 'Solicitud_Partes_Capex'),
    ('Actividad_Adicional', 'Actividad_Adicional'),
    ('Desmonte Equipos', 'Desmonte Equipos'),
    ('En_Instalacion', 'En_Instalacion'),
    ('En_Integracion', 'En_Integracion'),
    ('HW_Recibido', 'HW_Recibido'),
    ('Revisar_Pendientes', 'Revisar_Pendientes'),
    ('Acceso_Administrativo', 'Acceso_Administrativo'),
    ('Permiso_Acceso', 'Permiso_Acceso'),
    ('Performance_SS', 'Performance_SS'),
    ('Detenido_Cosite', 'Detenido_Cosite'),
    ('Pendiente_RFE', 'Pendiente_RFE'),
    ('Detenido_TSS', 'Detenido_TSS'),
    ('En_Transito', 'En_Transito'),
    ('TX', 'TX'),
    ('Pendiente_RFD', 'Pendiente_RFD'),
    ('Pendiente_RSH', 'Pendiente_RSH'),
    ('En_Programacion', 'En_Programacion'),
    ('Pendiente_HW', 'Pendiente_HW'),
    ('Solicitud_Despacho', 'Solicitud_Despacho'),
    ('Despacho_Solicitado', 'Despacho_Solicitado'),
    ('TSS', 'TSS'),
    ('Detenido_Antena', 'Detenido_Antena'),
    ('Detenido_Acceso', 'Detenido_Acceso'),
    ('HW_Antena', 'HW_Antena'),
    ('Aprovisionamiento', 'Aprovisionamiento'),
    ('Detenido_Acceso_Reemplazar_Sitio', 'Detenido_Acceso_Reemplazar_Sitio'),
    ('HW', 'HW'),
    ('HSEQ', 'HSEQ'),
    ('Correccion_Agrupador', 'Correccion_Agrupador'),
    ('OnAir_Comunidades', 'OnAir_Comunidades'),
    ('CW_Claro', 'CW_Claro'),
    ('En_Programacion_ReportadoPreviamente', 'En_Programacion_ReportadoPreviamente'),
    ('Aval_Segunda_Visita', 'Aval_Segunda_Visita'),
    ('RSH', 'RSH'),
    ('Scope_Sale', 'Scope_Sale'),
    ('Error_Claro', 'Error_Claro'),
    ('Otros O&M', 'Otros O&M'),
    ('Evaluacion_Estructural', 'Evaluacion_Estructural'),
    ('Sin_ID_Abastecimiento', 'Sin_ID_Abastecimiento'),
    ('OV_LTE_CE', 'OV_LTE_CE'),
    ('Reactivado', 'Reactivado'),
    ('Detenido_Robo', 'Detenido_Robo'),
    ('Instalacion_ReportadaPreviamente', 'Instalacion_ReportadaPreviamente'),
    ('Material_Faltante', 'Material_Faltante'),
    ('Antena', 'Antena'),
    ('Cancelado_Claro', 'Cancelado_Claro'),
    ('Congelado', 'Congelado'),
    ('Detenido_Orden_Publico', 'Detenido_Orden_Publico'),
    ('HW_Parcial', 'HW_Parcial'),
    ('Cancelado', 'Cancelado'),
    ('Programacion_Pendiente2016', 'Programacion_Pendiente2016'),
    ('Detenido_HSEQ', 'Detenido_HSEQ'),
)

""" BOLSA_CHOICES  """
BOLSA_CHOICES = (
    # ('', '---------'),
    ('55 sitios LSM', '55 sitios LSM'),
    ('165 sitios LSM', '165 sitios LSM'),
    ('170 sitios LSM', '170 sitios LSM'),
    ('531 sitios LSM', '531 sitios LSM'),
    ('Sitios Bulk', 'Sitios Bulk'),
    ('Airscale 167', 'Airscale 167'),
    ('381 sitios LSM Mixto (Airscale + FSMF)', '381 sitios LSM Mixto (Airscale + FSMF)'),
    ('114 sitios LSM Mixto (Airscale + FSMF)', '114 sitios LSM Mixto (Airscale + FSMF)'),
    ('Reemplazo 170 sitios LSM', 'Reemplazo 170 sitios LSM'),
    ('36 sitios Satelitales LSM', '36 sitios Satelitales LSM'),
    ('Reemplazo 36 sitios Satelitales LSM', 'Reemplazo 36 sitios Satelitales LSM'),
    ('Partes 302 sitios LSM', 'Partes 302 sitios LSM'),
    ('Pendiente Pedido', 'Pendiente Pedido'),
)

""" SATELITAL_CHOICES  """
SATELITAL_CHOICES = (
    ('', '---------'),
    ('Satelital', 'Satelital'),
)

""" COMUNIDADES_CHOICES  """
COMUNIDADES_CHOICES = (
    ('', '---------'),
    ('142 Comunidades P1', '142 Comunidades P1'),
    ('142 Comunidades P1', '142 Comunidades P2'),
    ('142 Comunidades P1', '142 Comunidades P3'),
)

""" IMPACTAR_CHOICES  """
IMPACTAR_CHOICES = (
    ('Si', 'Si'),
    ('No', 'No'),
)
