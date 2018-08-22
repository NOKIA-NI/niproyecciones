from celery import shared_task, current_task
from .models import (
    AsignacionBulk,
    AsignacionAntena,
    EstadoPo,
    PoZina,
    SitioBolsa,
    SitioBulk,
    SitioPo,
    )
from estaciones.models import Estacion
from partes.models import Parte
from hw_proyecciones.models import HwSiteList, HwControlRfe

@shared_task
def task_sitios_asignacion():
    current_task.update_state(state='PROGRESS')
    SitioBolsa.objects.all().delete()
    SitioBulk.objects.all().delete()
    # status_nokia = ['Complete Sites (Installed)', 'Parcial FXCB', 'Parcial Jumpers', 'Complete Sites (Por Armar LSM)']
    status_nokia = ['Piloto 1']
    sitios_asignacion = HwSiteList.objects.filter(status_nokia__in=status_nokia, solicitud_hw='1', estado_HW='NO CONFIRMADO')
    Bolsa_HW = ['Sitios Bulk', 'LSM A BULK']
    sitios_asignacion_bolsa = sitios_asignacion.exclude(Bolsa_HW__in=Bolsa_HW)
    sitios_asignacion_bulk = sitios_asignacion.filter(Bolsa_HW__in=Bolsa_HW)
    for sitio_asignacion_bolsa in sitios_asignacion_bolsa:
        sitio_bolsa = SitioBolsa.objects.create(
            estacion=Estacion.objects.get(site_name__iexact=sitio_asignacion_bolsa.siteName)
        )
    for sitio_asignacion_bulk in sitios_asignacion_bulk:
        sitio_bolsa = SitioBulk.objects.create(
            estacion=Estacion.objects.get(site_name__iexact=sitio_asignacion_bulk.siteName)
        )
    return { 'ok':200 }

@shared_task
def task_sitios_po():
    current_task.update_state(state='PROGRESS')
    sitios_bolsa = SitioBolsa.objects.all()
    list_site_name = [ sitio.estacion.site_name for sitio in sitios_bolsa ]
    sitios_pos_zina = PoZina.objects.filter(site_name__in=list_site_name)
    list_pos_zina = [ pos_zina.cpo_number for pos_zina in sitios_pos_zina ]
    list_pos_zina = list(set(list_pos_zina))
    estados_po = EstadoPo.objects.filter(numero_po__in=list_pos_zina)
    SitioPo.objects.all().delete()
    for estado_po in estados_po:
        sitio_po = SitioPo.objects.create(
            numero_po=estado_po.numero_po,
            estacion=estado_po.estacion,
            bts=estado_po.bts,
            bts_status=estado_po.bts_status,
            jumper=estado_po.jumper,
            jumper_status=estado_po.jumper_status,
            fxcb=estado_po.fxcb,
            fxcb_status=estado_po.fxcb_status,
        )
    return { 'ok':200 }

@shared_task
def task_asignacion_bolsa():
    current_task.update_state(state='PROGRESS')
    sitios_po = SitioPo.objects.filter(bts_status='AVAILABLE IN WH') # filtra sitios por po's AVAILABLE IN WH
    list_sitio_po = [ sitio_po.numero_po for sitio_po in sitios_po ]
    sitios_pos_zina = PoZina.objects.filter(cpo_number__in=list_sitio_po) # filtra sitios en zina por po's AVAILABLE IN WH
    list_site_name = [ sitio.site_name for sitio in sitios_pos_zina ]
    list_site_name = list(set(list_site_name)) # elimina items duplicados
    sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__in=list_site_name) # filtra sitios en rfe por po's zina
    for sitio_hw_control_rfe in sitios_hw_control_rfe: # for principal
        if sitio_hw_control_rfe.total_smr == 0: # la necesidad es 0
            sitio_hw_control_rfe.so = 'N/A'
            sitio_hw_control_rfe.po = 'N/A'
            sitio_hw_control_rfe.bodega_origen = 'N/A'
            sitio_hw_control_rfe.save() # termina asignar
        else:
            PARTE = sitio_hw_control_rfe.parte
            if PARTE == 'AISG_4MTS': # homologacion
                PARTE = 'AISG_5MTS'
                sitio_hw_control_rfe.homologacion = 'AISG_5MTS'
                sitio_hw_control_rfe.save()
            if PARTE == 'FPCC':
                PARTE = 'FPCA'
                sitio_hw_control_rfe.homologacion = 'FPCA'
                sitio_hw_control_rfe.save()
            if PARTE == 'FPBA':
                PARTE = 'FPBB'
                sitio_hw_control_rfe.homologacion = 'FPBB'
                sitio_hw_control_rfe.save()
            if PARTE == 'J_MR_MA_8MTS_SUPERFLEX':
                PARTE = 'J_MR_MA_8MTS_DCLASS'
                sitio_hw_control_rfe.homologacion = 'J_MR_MA_8MTS_DCLASS'
                sitio_hw_control_rfe.save()
            if PARTE == 'J_HR_MA_4MTS_PREMIUM':
                PARTE = 'J_HR_MA_4MTS_DCLASS'
                sitio_hw_control_rfe.homologacion = 'J_HR_MA_4MTS_DCLASS'
                sitio_hw_control_rfe.save()
            if PARTE == 'FMCF':
                PARTE = 'FMCA'
                sitio_hw_control_rfe.homologacion = 'FMCA'
                sitio_hw_control_rfe.save()
            if PARTE == 'FYTG':
                PARTE = 'FUFAY'
                sitio_hw_control_rfe.homologacion = 'FUFAY'
                sitio_hw_control_rfe.save()
            if PARTE == 'FSFC':
                PARTE = 'FUFAY'
                sitio_hw_control_rfe.homologacion = 'FUFAY'
                sitio_hw_control_rfe.save()
            pos_zina = sitios_pos_zina.filter(site_name=sitio_hw_control_rfe.siteName, parte_capex=PARTE) # filtra por sitio y parte
            if pos_zina.count() == 0: # no hay po en Zina
                count = 0
                switch = True # switch encendido
                if (PARTE == 'FCOB'\
                or PARTE == 'AMIA'\
                or PARTE == 'ABIA'\
                or PARTE == 'ASIA')\
                and sitio_hw_control_rfe.total_smr > 0: # kit air scale
                    kit_air_scale = sitios_pos_zina.get(site_name=sitio_hw_control_rfe.siteName, parte_capex='AirScale Base Setup Outdoor Rack + Shelf + 1 ASIA + 1 ABIA')
                    if kit_air_scale:
                        if kit_air_scale.quantity == 1 and (not sitio_hw_control_rfe.so or sitio_hw_control_rfe.so is None):
                            list_fcob = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FCOB')
                            for fcob in list_fcob:
                                if fcob.total_smr > 1:
                                    fcobs_zina = sitios_pos_zina.filter(site_name=fcob.siteName, parte_capex=fcob.parte)
                                    for fcob_zina in fcobs_zina:
                                        if fcob_zina.quantity - fcob.total_smr + 1 >= 0:
                                            fcob.so = sitio_po.bts
                                            fcob.po = str(sitio_po.numero_po) + 'X' + str(fcob.total_smr)
                                            fcob.bodega_origen = 'Panalpina'
                                            fcob.save()
                                            fcob_zina.quantity = fcob_zina.quantity - fcob.total_smr + 1
                                            fcob_zina.save()
                                            break
                                        else:
                                            fcob.so = sitio_po.bts
                                            fcob.po = str(sitio_po.numero_po) + 'X' + str(fcob_zina.quantity + 1)
                                            fcob.bodega_origen = 'Panalpina'
                                            fcob.save()
                                            fcob_zina.quantity = 0
                                            fcob_zina.save()
                                            try:
                                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=fcob.parte)
                                                if (asignacion_bulk.cantidad - fcob.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                    fcob.issue_bodega_origen = 'FaltanteX' + str(fcob.total_smr - fcob_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                    fcob.save() # termina asignar
                                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - fcob.total_smr + 1
                                                    asignacion_bulk.save() # modifica cantidad
                                                else:
                                                    fcob.issue_bodega_origen = 'FaltanteX' + str(fcob.total_smr - fcob_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    fcob.save() # termina asignar
                                            except AsignacionBulk.DoesNotExist:
                                                fcob.issue_bodega_origen = 'FaltanteX' + str(fcob.total_smr - fcob_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                fcob.save() # termina asignar 
                                if fcob.total_smr == 1:
                                    fcob.so = sitio_po.bts
                                    fcob.po = str(sitio_po.numero_po) + 'X1'
                                    fcob.bodega_origen = 'Panalpina'
                                    fcob.save()
                                    break
                            list_amia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='AMIA')
                            for amia in list_amia:
                                if amia.total_smr > 1:
                                    amias_zina = sitios_pos_zina.filter(site_name=amia.siteName, parte_capex=amia.parte)
                                    for amia_zina in amias_zina:
                                        if amia_zina.quantity - amia.total_smr + 1 >= 0:
                                            amia.so = sitio_po.bts
                                            amia.po = str(sitio_po.numero_po) + 'X' + str(amia.total_smr)
                                            amia.bodega_origen = 'Panalpina'
                                            amia.save()
                                            amia_zina.quantity = amia_zina.quantity - amia.total_smr + 1
                                            amia_zina.save()
                                            break
                                        else:
                                            amia.so = sitio_po.bts
                                            amia.po = str(sitio_po.numero_po) + 'X' + str(amia_zina.quantity + 1)
                                            amia.bodega_origen = 'Panalpina'
                                            amia.save()
                                            amia_zina.quantity = 0
                                            amia_zina.save()
                                            try:
                                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=amia.parte)
                                                if (asignacion_bulk.cantidad - amia.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                    amia.issue_bodega_origen = 'FaltanteX' + str(amia.total_smr - amia_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                    amia.save() # termina asignar
                                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - amia.total_smr + 1
                                                    asignacion_bulk.save() # modifica cantidad
                                                else:
                                                    amia.issue_bodega_origen = 'FaltanteX' + str(amia.total_smr - amia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    amia.save() # termina asignar
                                            except AsignacionBulk.DoesNotExist:
                                                amia.issue_bodega_origen = 'FaltanteX' + str(amia.total_smr - amia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                amia.save() # termina asignar 
                                if amia.total_smr == 1:
                                    amia.so = sitio_po.bts
                                    amia.po = str(sitio_po.numero_po) + 'X1'
                                    amia.bodega_origen = 'Panalpina'
                                    amia.save()
                                    break
                            list_abia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='ABIA')
                            for abia in list_abia:
                                if abia.total_smr > 1:
                                    abias_zina = sitios_pos_zina.filter(site_name=abia.siteName, parte_capex=abia.parte)
                                    for abia_zina in abias_zina:
                                        if abia_zina.quantity - abia.total_smr + 1 >= 0:
                                            abia.so = sitio_po.bts
                                            abia.po = str(sitio_po.numero_po) + 'X' + str(abia.total_smr)
                                            abia.bodega_origen = 'Panalpina'
                                            abia.save()
                                            abia_zina.quantity = abia_zina.quantity - abia.total_smr + 1
                                            abia_zina.save()
                                            break
                                        else:
                                            abia.so = sitio_po.bts
                                            abia.po = str(sitio_po.numero_po) + 'X' + str(abia_zina.quantity + 1)
                                            abia.bodega_origen = 'Panalpina'
                                            abia.save()
                                            abia_zina.quantity = 0
                                            abia_zina.save()
                                            try:
                                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=abia.parte)
                                                if (asignacion_bulk.cantidad - abia.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                    abia.issue_bodega_origen = 'FaltanteX' + str(abia.total_smr - abia_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                    abia.save() # termina asignar
                                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - abia.total_smr + 1
                                                    asignacion_bulk.save() # modifica cantidad
                                                else:
                                                    abia.issue_bodega_origen = 'FaltanteX' + str(abia.total_smr - abia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    abia.save() # termina asignar
                                            except AsignacionBulk.DoesNotExist:
                                                abia.issue_bodega_origen = 'FaltanteX' + str(abia.total_smr - abia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                abia.save() # termina asignar 
                                if abia.total_smr == 1:
                                    abia.so = sitio_po.bts
                                    abia.po = str(sitio_po.numero_po) + 'X1'
                                    abia.bodega_origen = 'Panalpina'
                                    abia.save()
                                    break
                            list_asia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='ASIA')
                            for asia in list_asia:
                                if asia.total_smr > 1:
                                    asias_zina = sitios_pos_zina.filter(site_name=asia.siteName, parte_capex=asia.parte)
                                    for asia_zina in asias_zina:
                                        if asia_zina.quantity - asia.total_smr + 1 >= 0:
                                            asia.so = sitio_po.bts
                                            asia.po = str(sitio_po.numero_po) + 'X' + str(asia.total_smr)
                                            asia.bodega_origen = 'Panalpina'
                                            asia.save()
                                            asia_zina.quantity = asia_zina.quantity - asia.total_smr + 1
                                            asia_zina.save()
                                            break
                                        else:
                                            asia.so = sitio_po.bts
                                            asia.po = str(sitio_po.numero_po) + 'X' + str(asia_zina.quantity + 1)
                                            asia.bodega_origen = 'Panalpina'
                                            asia.save()
                                            asia_zina.quantity = 0
                                            asia_zina.save()
                                            try:
                                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=asia.parte)
                                                if (asignacion_bulk.cantidad - asia.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                    asia.issue_bodega_origen = 'FaltanteX' + str(asia.total_smr - asia_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                    asia.save() # termina asignar
                                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - asia.total_smr + 1
                                                    asignacion_bulk.save() # modifica cantidad
                                                else:
                                                    asia.issue_bodega_origen = 'FaltanteX' + str(asia.total_smr - asia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    asia.save() # termina asignar
                                            except AsignacionBulk.DoesNotExist:
                                                asia.issue_bodega_origen = 'FaltanteX' + str(asia.total_smr - asia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                asia.save() # termina asignar 
                                if asia.total_smr == 1:
                                    asia.so = sitio_po.bts
                                    asia.po = str(sitio_po.numero_po) + 'X1'
                                    asia.bodega_origen = 'Panalpina'
                                    asia.save()
                                    break
                            kit_air_scale.quantity = 0
                            kit_air_scale.save()
                            switch = False # switch apagado
                if PARTE == 'FYMA'\
                or PARTE == 'FTSE'\
                or PARTE == 'FYGB': # kit gps
                    kit_gps = sitios_pos_zina.get(site_name=sitio_hw_control_rfe.siteName, parte_capex='GPS receiver FYGB FYMA FTSE kit')
                    if kit_gps:
                        if kit_gps.quantity == 1 and (not sitio_hw_control_rfe.so or sitio_hw_control_rfe.so is None):
                            list_fyma = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FYMA')
                            for fyma in list_fyma:
                                fyma.so = sitio_po.bts
                                fyma.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                fyma.bodega_origen = 'Panalpina'
                                fyma.save()
                                break
                            list_ftse = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FTSE')
                            for ftse in list_ftse:
                                ftse.so = sitio_po.bts
                                ftse.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                ftse.bodega_origen = 'Panalpina'
                                ftse.save()
                                break
                            list_fygb = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FYGB')
                            for fygb in list_fygb:
                                fygb.so = sitio_po.bts
                                fygb.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                fygb.bodega_origen = 'Panalpina'
                                fygb.save()
                                break
                            kit_gps.quantity = 0
                            kit_gps.save()
                            switch = False # switch apagado
                if switch:# si el switch encendido
                    try:
                        asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                        if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                            sitio_hw_control_rfe.so = asignacion_bulk.so
                            sitio_hw_control_rfe.po = asignacion_bulk.po
                            sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                            sitio_hw_control_rfe.issue_bodega_origen = asignacion_bulk.comentario_bodega
                            sitio_hw_control_rfe.save() # termina asignar
                            asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                            asignacion_bulk.save() # modifica cantidad
                    except AsignacionBulk.DoesNotExist:
                        pass
            if pos_zina.count() == 1: # hay una po en zina
                count = 0
                for po_zina in pos_zina:
                    switch = True # switch encendido
                    if (PARTE == 'FCOB'\
                    or PARTE == 'AMIA'\
                    or PARTE == 'ABIA'\
                    or PARTE == 'ASIA')\
                    and sitio_hw_control_rfe.total_smr > 0: # kit air scale
                        kit_air_scale = sitios_pos_zina.get(site_name=sitio_hw_control_rfe.siteName, parte_capex='AirScale Base Setup Outdoor Rack + Shelf + 1 ASIA + 1 ABIA')
                        if kit_air_scale:
                            if kit_air_scale.quantity == 1 and (not sitio_hw_control_rfe.so or sitio_hw_control_rfe.so is None):
                                list_fcob = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FCOB')
                                for fcob in list_fcob:
                                    if fcob.total_smr > 1:
                                        fcobs_zina = sitios_pos_zina.filter(site_name=fcob.siteName, parte_capex=fcob.parte)
                                        for fcob_zina in fcobs_zina:
                                            if fcob_zina.quantity - fcob.total_smr + 1 >= 0:
                                                fcob.so = sitio_po.bts
                                                fcob.po = str(sitio_po.numero_po) + 'X' + str(fcob.total_smr)
                                                fcob.bodega_origen = 'Panalpina'
                                                fcob.save()
                                                fcob_zina.quantity = fcob_zina.quantity - fcob.total_smr + 1
                                                fcob_zina.save()
                                                break
                                            else:
                                                fcob.so = sitio_po.bts
                                                fcob.po = str(sitio_po.numero_po) + 'X' + str(fcob_zina.quantity + 1)
                                                fcob.bodega_origen = 'Panalpina'
                                                fcob.save()
                                                fcob_zina.quantity = 0
                                                fcob_zina.save()
                                                try:
                                                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=fcob.parte)
                                                    if (asignacion_bulk.cantidad - fcob.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                        fcob.issue_bodega_origen = 'FaltanteX' + str(fcob.total_smr - fcob_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                        fcob.save() # termina asignar
                                                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - fcob.total_smr + 1
                                                        asignacion_bulk.save() # modifica cantidad
                                                    else:
                                                        fcob.issue_bodega_origen = 'FaltanteX' + str(fcob.total_smr - fcob_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                        fcob.save() # termina asignar
                                                except AsignacionBulk.DoesNotExist:
                                                    fcob.issue_bodega_origen = 'FaltanteX' + str(fcob.total_smr - fcob_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    fcob.save() # termina asignar 
                                    if fcob.total_smr == 1:
                                        fcob.so = sitio_po.bts
                                        fcob.po = str(sitio_po.numero_po) + 'X1'
                                        fcob.bodega_origen = 'Panalpina'
                                        fcob.save()
                                        break
                                list_amia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='AMIA')
                                for amia in list_amia:
                                    if amia.total_smr > 1:
                                        amias_zina = sitios_pos_zina.filter(site_name=amia.siteName, parte_capex=amia.parte)
                                        for amia_zina in amias_zina:
                                            if amia_zina.quantity - amia.total_smr + 1 >= 0:
                                                amia.so = sitio_po.bts
                                                amia.po = str(sitio_po.numero_po) + 'X' + str(amia.total_smr)
                                                amia.bodega_origen = 'Panalpina'
                                                amia.save()
                                                amia_zina.quantity = amia_zina.quantity - amia.total_smr + 1
                                                amia_zina.save()
                                                break
                                            else:
                                                amia.so = sitio_po.bts
                                                amia.po = str(sitio_po.numero_po) + 'X' + str(amia_zina.quantity + 1)
                                                amia.bodega_origen = 'Panalpina'
                                                amia.save()
                                                amia_zina.quantity = 0
                                                amia_zina.save()
                                                try:
                                                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=amia.parte)
                                                    if (asignacion_bulk.cantidad - amia.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                        amia.issue_bodega_origen = 'FaltanteX' + str(amia.total_smr - amia_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                        amia.save() # termina asignar
                                                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - amia.total_smr + 1
                                                        asignacion_bulk.save() # modifica cantidad
                                                    else:
                                                        amia.issue_bodega_origen = 'FaltanteX' + str(amia.total_smr - amia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                        amia.save() # termina asignar
                                                except AsignacionBulk.DoesNotExist:
                                                    amia.issue_bodega_origen = 'FaltanteX' + str(amia.total_smr - amia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    amia.save() # termina asignar 
                                    if amia.total_smr == 1:
                                        amia.so = sitio_po.bts
                                        amia.po = str(sitio_po.numero_po) + 'X1'
                                        amia.bodega_origen = 'Panalpina'
                                        amia.save()
                                        break
                                list_abia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='ABIA')
                                for abia in list_abia:
                                    if abia.total_smr > 1:
                                        abias_zina = sitios_pos_zina.filter(site_name=abia.siteName, parte_capex=abia.parte)
                                        for abia_zina in abias_zina:
                                            if abia_zina.quantity - abia.total_smr + 1 >= 0:
                                                abia.so = sitio_po.bts
                                                abia.po = str(sitio_po.numero_po) + 'X' + str(abia.total_smr)
                                                abia.bodega_origen = 'Panalpina'
                                                abia.save()
                                                abia_zina.quantity = abia_zina.quantity - abia.total_smr + 1
                                                abia_zina.save()
                                                break
                                            else:
                                                abia.so = sitio_po.bts
                                                abia.po = str(sitio_po.numero_po) + 'X' + str(abia_zina.quantity + 1)
                                                abia.bodega_origen = 'Panalpina'
                                                abia.save()
                                                abia_zina.quantity = 0
                                                abia_zina.save()
                                                try:
                                                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=abia.parte)
                                                    if (asignacion_bulk.cantidad - abia.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                        abia.issue_bodega_origen = 'FaltanteX' + str(abia.total_smr - abia_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                        abia.save() # termina asignar
                                                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - abia.total_smr + 1
                                                        asignacion_bulk.save() # modifica cantidad
                                                    else:
                                                        abia.issue_bodega_origen = 'FaltanteX' + str(abia.total_smr - abia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                        abia.save() # termina asignar
                                                except AsignacionBulk.DoesNotExist:
                                                    abia.issue_bodega_origen = 'FaltanteX' + str(abia.total_smr - abia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    abia.save() # termina asignar 
                                    if abia.total_smr == 1:
                                        abia.so = sitio_po.bts
                                        abia.po = str(sitio_po.numero_po) + 'X1'
                                        abia.bodega_origen = 'Panalpina'
                                        abia.save()
                                        break
                                list_asia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='ASIA')
                                for asia in list_asia:
                                    if asia.total_smr > 1:
                                        asias_zina = sitios_pos_zina.filter(site_name=asia.siteName, parte_capex=asia.parte)
                                        for asia_zina in asias_zina:
                                            if asia_zina.quantity - asia.total_smr + 1 >= 0:
                                                asia.so = sitio_po.bts
                                                asia.po = str(sitio_po.numero_po) + 'X' + str(asia.total_smr)
                                                asia.bodega_origen = 'Panalpina'
                                                asia.save()
                                                asia_zina.quantity = asia_zina.quantity - asia.total_smr + 1
                                                asia_zina.save()
                                                break
                                            else:
                                                asia.so = sitio_po.bts
                                                asia.po = str(sitio_po.numero_po) + 'X' + str(asia_zina.quantity + 1)
                                                asia.bodega_origen = 'Panalpina'
                                                asia.save()
                                                asia_zina.quantity = 0
                                                asia_zina.save()
                                                try:
                                                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=asia.parte)
                                                    if (asignacion_bulk.cantidad - asia.total_smr) + 1 > asignacion_bulk.cantidad * 0.1:
                                                        asia.issue_bodega_origen = 'FaltanteX' + str(asia.total_smr - asia_zina.quantity + 1) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                                        asia.save() # termina asignar
                                                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - asia.total_smr + 1
                                                        asignacion_bulk.save() # modifica cantidad
                                                    else:
                                                        asia.issue_bodega_origen = 'FaltanteX' + str(asia.total_smr - asia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                        asia.save() # termina asignar
                                                except AsignacionBulk.DoesNotExist:
                                                    asia.issue_bodega_origen = 'FaltanteX' + str(asia.total_smr - asia_zina.quantity + 1) + ' Sin diponibilidad en bodega'
                                                    asia.save() # termina asignar 
                                    if asia.total_smr == 1:
                                        asia.so = sitio_po.bts
                                        asia.po = str(sitio_po.numero_po) + 'X1'
                                        asia.bodega_origen = 'Panalpina'
                                        asia.save()
                                        break
                                kit_air_scale.quantity = 0
                                kit_air_scale.save()
                                switch = False # switch apagado
                    if PARTE == 'FYMA'\
                    or PARTE == 'FTSE'\
                    or PARTE == 'FYGB': # kit gps
                        kit_gps = sitios_pos_zina.get(site_name=sitio_hw_control_rfe.siteName, parte_capex='GPS receiver FYGB FYMA FTSE kit')
                        if kit_gps:
                            if kit_gps.quantity == 1 and (not sitio_hw_control_rfe.so or sitio_hw_control_rfe.so is None):
                                list_fyma = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FYMA')
                                for fyma in list_fyma:
                                    fyma.so = sitio_po.bts
                                    fyma.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    fyma.bodega_origen = 'Panalpina'
                                    fyma.save()
                                    break
                                list_ftse = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FTSE')
                                for ftse in list_ftse:
                                    ftse.so = sitio_po.bts
                                    ftse.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    ftse.bodega_origen = 'Panalpina'
                                    ftse.save()
                                    break
                                list_fygb = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FYGB')
                                for fygb in list_fygb:
                                    fygb.so = sitio_po.bts
                                    fygb.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    fygb.bodega_origen = 'Panalpina'
                                    fygb.save()
                                    break
                                kit_gps.quantity = 0
                                kit_gps.save()
                                switch = False # switch apagado
                    if PARTE == 'J_MR_MA_4MTS_DCLASS'\
                    or PARTE == 'J_MR_MA_8MTS_DCLASS'\
                    or PARTE == 'J_MR_MA_14MTS_DCLASS':
                        sitio_po = SitioPo.objects.get(numero_po=po_zina.cpo_number)
                        if sitio_po.jumper_status != 'AVAILABLE IN WH': # asignar bulk
                            try:
                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                                if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                    sitio_hw_control_rfe.so = asignacion_bulk.so
                                    sitio_hw_control_rfe.po = asignacion_bulk.po
                                    sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                    sitio_hw_control_rfe.issue_bodega_origen = asignacion_bulk.comentario_bodega
                                    sitio_hw_control_rfe.save() # termina asignar
                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                    asignacion_bulk.save() # modifica cantidad
                                    switch = False # switch apagado
                            except AsignacionBulk.DoesNotExist:
                                pass
                    if sitio_hw_control_rfe == 'FXCB':
                        sitio_po = SitioPo.objects.get(numero_po=po_zina.cpo_number)
                        if sitio_po.fxcb == 'FXCB separated' and sitio_po.fxcb_status != 'AVAILABLE IN WH': # asignar bulk
                            try:
                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                                if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                    sitio_hw_control_rfe.so = asignacion_bulk.so
                                    sitio_hw_control_rfe.po = asignacion_bulk.po
                                    sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                    sitio_hw_control_rfe.issue_bodega_origen = asignacion_bulk.comentario_bodega
                                    sitio_hw_control_rfe.save() # termina asignar
                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                    asignacion_bulk.save() # modifica cantidad
                                    switch = False # switch apagado
                            except AsignacionBulk.DoesNotExist:
                                pass
                    if switch:# si el switch encendido
                        if po_zina.quantity == 0: # asignar bulk
                            try:
                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                                if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                    sitio_hw_control_rfe.so = asignacion_bulk.so
                                    sitio_hw_control_rfe.po = asignacion_bulk.po
                                    sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                    sitio_hw_control_rfe.issue_bodega_origen = asignacion_bulk.comentario_bodega
                                    sitio_hw_control_rfe.save() # termina asignar
                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                    asignacion_bulk.save() # modifica cantidad
                            except AsignacionBulk.DoesNotExist:
                                pass
                        if po_zina.quantity > 0: # asignar
                            if po_zina.quantity - sitio_hw_control_rfe.total_smr >= 0: # asignar po
                                sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                if PARTE == 'J_MR_MA_4MTS_DCLASS'\
                                or PARTE == 'J_MR_MA_8MTS_DCLASS'\
                                or PARTE == 'J_MR_MA_14MTS_DCLASS':
                                    sitio_hw_control_rfe.so = sitio_po.jumper
                                else:
                                    sitio_hw_control_rfe.so = sitio_po.bts
                                sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                sitio_hw_control_rfe.save() # termina asignar
                                po_zina.quantity = po_zina.quantity - sitio_hw_control_rfe.total_smr
                                po_zina.save() # modifica quantity
                            else:
                                if PARTE == 'Amphenol_2x16'\
                                or PARTE == 'Amphenol_2x25'\
                                or PARTE == 'Amphenol_2x35':
                                    try:
                                        asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                                        if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                            sitio_hw_control_rfe.so = asignacion_bulk.so
                                            sitio_hw_control_rfe.po = asignacion_bulk.po
                                            sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                            sitio_hw_control_rfe.issue_bodega_origen = asignacion_bulk.comentario_bodega
                                            sitio_hw_control_rfe.save() # termina asignar
                                            asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                            asignacion_bulk.save() # modifica cantidad
                                            break
                                    except AsignacionBulk.DoesNotExist:
                                        pass
                                count = po_zina.quantity
                                sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                if PARTE == 'J_MR_MA_4MTS_DCLASS'\
                                or PARTE == 'J_MR_MA_8MTS_DCLASS'\
                                or PARTE == 'J_MR_MA_14MTS_DCLASS':
                                    sitio_hw_control_rfe.so = sitio_po.jumper
                                else:
                                    sitio_hw_control_rfe.so = sitio_po.bts
                                sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(po_zina.quantity)
                                sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                sitio_hw_control_rfe.save() # termina asignar
                                po_zina.quantity -= po_zina.quantity
                                po_zina.save() # modifica quantity
                                try:
                                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                                    if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                        sitio_hw_control_rfe.issue_bodega_origen = 'FaltanteX' + str(sitio_hw_control_rfe.total_smr - count) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                                        sitio_hw_control_rfe.save() # termina asignar
                                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                        asignacion_bulk.save() # modifica cantidad
                                except AsignacionBulk.DoesNotExist:
                                    pass
            if pos_zina.count() > 1: # hay mas de una po en zina
                count = 0
                for po_zina in pos_zina:
                    switch = True # switch encendido
                    if (PARTE == 'FCOB'\
                    or PARTE == 'AMIA'\
                    or PARTE == 'ABIA'\
                    or PARTE == 'ASIA')\
                    and sitio_hw_control_rfe.total_smr == 1: # kit air scale
                        kit_air_scale = sitios_pos_zina.get(site_name=sitio_hw_control_rfe.siteName, parte_capex='AirScale Base Setup Outdoor Rack + Shelf + 1 ASIA + 1 ABIA')
                        if kit_air_scale:
                            if kit_air_scale.quantity == 1 and (not sitio_hw_control_rfe.so or sitio_hw_control_rfe.so is None):
                                list_fcob = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FCOB')
                                for fcob in list_fcob:
                                    fcob.so = sitio_po.bts
                                    fcob.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    fcob.bodega_origen = 'Panalpina'
                                    fcob.save()
                                    break
                                list_amia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='AMIA')
                                for amia in list_amia:
                                    amia.so = sitio_po.bts
                                    amia.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    amia.bodega_origen = 'Panalpina'
                                    amia.save()
                                    break
                                list_abia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='ABIA')
                                for abia in list_abia:
                                    abia.so = sitio_po.bts
                                    abia.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    abia.bodega_origen = 'Panalpina'
                                    abia.save()
                                    break
                                list_asia = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='ASIA')
                                for asia in list_asia:
                                    asia.so = sitio_po.bts
                                    asia.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    asia.bodega_origen = 'Panalpina'
                                    asia.save()
                                    break
                                kit_air_scale.quantity = 0
                                kit_air_scale.save()
                                switch = False # switch apagado
                                break
                    if PARTE == 'FYMA'\
                    or PARTE == 'FTSE'\
                    or PARTE == 'FYGB': # kit gps
                        kit_gps = sitios_pos_zina.get(site_name=sitio_hw_control_rfe.siteName, parte_capex='GPS receiver FYGB FYMA FTSE kit')
                        if kit_gps:
                            if kit_gps.quantity == 1 and (not sitio_hw_control_rfe.so or sitio_hw_control_rfe.so is None):
                                list_fyma = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FYMA')
                                for fyma in list_fyma:
                                    sitio_hw_control_rfe.so = sitio_po.bts
                                    sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                    sitio_hw_control_rfe.save()
                                    break
                                list_ftse = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FTSE')
                                for ftse in list_ftse:
                                    sitio_hw_control_rfe.so = sitio_po.bts
                                    sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                    sitio_hw_control_rfe.save()
                                    break
                                list_fygb = HwControlRfe.objects.filter(siteName=sitio_hw_control_rfe.siteName, parte='FYGB')
                                for fygb in list_fygb:
                                    sitio_hw_control_rfe.so = sitio_po.bts
                                    sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                    sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                    sitio_hw_control_rfe.save()
                                    break
                                kit_gps.quantity = 0
                                kit_gps.save()
                                switch = False # switch apagado
                                break
                    if PARTE == 'J_MR_MA_4MTS_DCLASS'\
                    or PARTE == 'J_MR_MA_8MTS_DCLASS'\
                    or PARTE == 'J_MR_MA_14MTS_DCLASS':
                        sitio_po = SitioPo.objects.get(numero_po=po_zina.cpo_number)
                        if sitio_po.jumper_status != 'AVAILABLE IN WH': # asignar bulk
                            switch = False # switch apagado
                    if sitio_hw_control_rfe == 'FXCB':
                        sitio_po = SitioPo.objects.get(numero_po=po_zina.cpo_number)
                        if sitio_po.fxcb == 'FXCB separated' and sitio_po.fxcb_status != 'AVAILABLE IN WH': # asignar bulk
                            switch = False # switch apagado
                    if switch:# si el switch encendido
                        if po_zina.quantity > 0: # asignar
                            if (po_zina.quantity - sitio_hw_control_rfe.total_smr) + count >= 0: # asignar po
                                if count > 0:
                                    sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                    if PARTE == 'J_MR_MA_4MTS_DCLASS'\
                                    or PARTE == 'J_MR_MA_8MTS_DCLASS'\
                                    or PARTE == 'J_MR_MA_14MTS_DCLASS':
                                        sitio_hw_control_rfe.so = str(sitio_hw_control_rfe.so) + '+' + str(sitio_po.jumper)
                                    else:
                                        sitio_hw_control_rfe.so = str(sitio_hw_control_rfe.so) + '+' + str(sitio_po.bts)
                                    sitio_hw_control_rfe.po = str(sitio_hw_control_rfe.po) + '+' + str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr - count)
                                    sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                    sitio_hw_control_rfe.save() # termina asignar
                                    po_zina.quantity = (po_zina.quantity - sitio_hw_control_rfe.total_smr) + count
                                    po_zina.save() # modifica quantity
                                    count = -1
                                    break
                                sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                sitio_hw_control_rfe.so = sitio_po.bts
                                sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                sitio_hw_control_rfe.save() # termina asignar
                                po_zina.quantity = po_zina.quantity - sitio_hw_control_rfe.total_smr
                                po_zina.save() # modifica quantity
                                count = -1
                                break
                            if (po_zina.quantity - sitio_hw_control_rfe.total_smr) + count < 0: # asignar po
                                if PARTE == 'Amphenol_2x16'\
                                or PARTE == 'Amphenol_2x25'\
                                or PARTE == 'Amphenol_2x35':
                                    pass
                                else:
                                    if count > 0:
                                        count += po_zina.quantity
                                        sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                        if PARTE == 'J_MR_MA_4MTS_DCLASS'\
                                        or PARTE == 'J_MR_MA_8MTS_DCLASS'\
                                        or PARTE == 'J_MR_MA_14MTS_DCLASS':
                                            sitio_hw_control_rfe.so = str(sitio_hw_control_rfe.so) + '+' + str(sitio_po.jumper)
                                        else:
                                            sitio_hw_control_rfe.so = str(sitio_hw_control_rfe.so) + '+' + str(sitio_po.bts)
                                        sitio_hw_control_rfe.po = str(sitio_hw_control_rfe.po) + '+' + str(sitio_po.numero_po) + 'X' + str(po_zina.quantity)
                                        sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                        sitio_hw_control_rfe.save() # termina asignar
                                        po_zina.quantity -= po_zina.quantity
                                        po_zina.save() # modifica quantity
                                    if count == 0:
                                        count += po_zina.quantity
                                        sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                        if PARTE == 'J_MR_MA_4MTS_DCLASS'\
                                        or PARTE == 'J_MR_MA_8MTS_DCLASS'\
                                        or PARTE == 'J_MR_MA_14MTS_DCLASS':
                                            sitio_hw_control_rfe.so = sitio_po.jumper
                                        else:
                                            sitio_hw_control_rfe.so = sitio_po.bts
                                        sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(po_zina.quantity)
                                        sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                        sitio_hw_control_rfe.save() # termina asignar
                                        po_zina.quantity -= po_zina.quantity
                                        po_zina.save() # modifica quantity
                if count > 0: # asignar bulk
                    try:
                        asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                        if (asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr) + count > asignacion_bulk.cantidad * 0.1:
                            sitio_hw_control_rfe.issue_bodega_origen = 'FaltanteX' + str(sitio_hw_control_rfe.total_smr - count) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                            sitio_hw_control_rfe.save() # termina asignar
                            asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                            asignacion_bulk.save() # modifica cantidad
                    except AsignacionBulk.DoesNotExist:
                        pass
                if count == 0: # asignar bulk
                        try:
                            asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
                            if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                sitio_hw_control_rfe.so = asignacion_bulk.so
                                sitio_hw_control_rfe.po = asignacion_bulk.po
                                sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                sitio_hw_control_rfe.issue_bodega_origen = asignacion_bulk.comentario_bodega
                                sitio_hw_control_rfe.save() # termina asignar
                                asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                asignacion_bulk.save() # modifica cantidad
                        except AsignacionBulk.DoesNotExist:
                            pass
    return { 'ok':200 }

@shared_task
def task_sobrantes():
    current_task.update_state(state='PROGRESS')
    sitios_po = SitioPo.objects.filter(bts_status='AVAILABLE IN WH') # filtra sitios por po's AVAILABLE IN WH
    list_sitio_po = [ sitio_po.numero_po for sitio_po in sitios_po ]
    sitios_pos_zina = PoZina.objects.filter(cpo_number__in=list_sitio_po) # filtra sitios en zina por po's AVAILABLE IN WH
    sitios_pos_zina = sitios_pos_zina.filter(quantity__gt=0) # sobrantes
    for sitio_po_zina in sitios_pos_zina:
        if sitio_po_zina.parte_capex == 'J_MR_MA_4MTS_DCLASS'\
        or sitio_po_zina.parte_capex == 'J_MR_MA_8MTS_DCLASS'\
        or sitio_po_zina.parte_capex == 'J_MR_MA_14MTS_DCLASS' and sitios_po.get(numero_po=sitio_po_zina.cpo_number).jumper_status != 'AVAILABLE IN WH':
            pass
        elif sitio_po_zina.parte_capex == 'FXCB'\
        and sitios_po.get(numero_po=sitio_po_zina.cpo_number).fxcb_status != 'AVAILABLE IN WH'\
        and sitios_po.get(numero_po=sitio_po_zina.cpo_number).fxcb == 'FXCB separated':
            pass
        else:
            sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__iexact=sitio_po_zina.site_name, parte=sitio_po_zina.parte_capex) # sitios filtro rfe
            if sitios_hw_control_rfe.count() > 0:
                for sitio_hw_control_rfe in sitios_hw_control_rfe:
                    if sitio_hw_control_rfe.total_smr > 0:
                        if sitio_po_zina.quantity < 10:
                            if sitio_hw_control_rfe.material_sobrante:
                                sitio_hw_control_rfe.material_sobrante += '00' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                            else:
                                sitio_hw_control_rfe.material_sobrante = '00' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                        if sitio_po_zina.quantity >= 10 and sitio_po_zina.quantity < 100:
                            if sitio_hw_control_rfe.material_sobrante:
                                sitio_hw_control_rfe.material_sobrante += '0' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                            else:
                                sitio_hw_control_rfe.material_sobrante = '0' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                        if sitio_po_zina.quantity >= 100:
                            if sitio_hw_control_rfe.material_sobrante:
                                sitio_hw_control_rfe.material_sobrante += str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                            else:
                                sitio_hw_control_rfe.material_sobrante = str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                        break
                    else:
                        sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__iexact=sitio_po_zina.site_name)
                        for sitio_hw_control_rfe in sitios_hw_control_rfe:
                            if sitio_hw_control_rfe.total_smr > 0:
                                if sitio_po_zina.quantity < 10:
                                    if sitio_hw_control_rfe.material_sobrante:
                                        sitio_hw_control_rfe.material_sobrante += '00' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                        sitio_hw_control_rfe.save()
                                    else:
                                        sitio_hw_control_rfe.material_sobrante = '00' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                        sitio_hw_control_rfe.save()
                                if sitio_po_zina.quantity >= 10 and sitio_po_zina.quantity < 100:
                                    if sitio_hw_control_rfe.material_sobrante:
                                        sitio_hw_control_rfe.material_sobrante += '0' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                        sitio_hw_control_rfe.save()
                                    else:
                                        sitio_hw_control_rfe.material_sobrante = '0' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                        sitio_hw_control_rfe.save()
                                if sitio_po_zina.quantity >= 100:
                                    if sitio_hw_control_rfe.material_sobrante:
                                        sitio_hw_control_rfe.material_sobrante += str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                        sitio_hw_control_rfe.save()
                                    else:
                                        sitio_hw_control_rfe.material_sobrante = str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                        sitio_hw_control_rfe.save()
                                break
                        break
            else:
                sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__iexact=sitio_po_zina.site_name)
                for sitio_hw_control_rfe in sitios_hw_control_rfe:
                    if sitio_hw_control_rfe.total_smr > 0:
                        if sitio_po_zina.quantity < 10:
                            if sitio_hw_control_rfe.material_sobrante:
                                sitio_hw_control_rfe.material_sobrante += '00' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                            else:
                                sitio_hw_control_rfe.material_sobrante = '00' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                        if sitio_po_zina.quantity >= 10 and sitio_po_zina.quantity < 100:
                            if sitio_hw_control_rfe.material_sobrante:
                                sitio_hw_control_rfe.material_sobrante += '0' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                            else:
                                sitio_hw_control_rfe.material_sobrante = '0' + str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                        if sitio_po_zina.quantity >= 100:
                            if sitio_hw_control_rfe.material_sobrante:
                                sitio_hw_control_rfe.material_sobrante += str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                            else:
                                sitio_hw_control_rfe.material_sobrante = str(sitio_po_zina.quantity) + 'X' + sitio_po_zina.parte_capex + 'X' + str(sitio_po_zina.cpo_number) + ','
                                sitio_hw_control_rfe.save()
                        break
    return { 'ok':200 }

@shared_task
def task_asignacion_bulk():
    current_task.update_state(state='PROGRESS')
    sitios_bulk = SitioBulk.objects.all()
    list_site_name = [ sitio.estacion.site_name for sitio in sitios_bulk ]
    sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__in=list_site_name) # filtra sitios bilk en rfe
    for sitio_hw_control_rfe in sitios_hw_control_rfe:
        PARTE = sitio_hw_control_rfe.parte
        if PARTE == 'AISG_4MTS': # homologacion
            PARTE = 'AISG_5MTS'
            sitio_hw_control_rfe.homologacion = 'AISG_5MTS'
            sitio_hw_control_rfe.save()
        if PARTE == 'FPCC':
            PARTE = 'FPCA'
            sitio_hw_control_rfe.homologacion = 'FPCA'
            sitio_hw_control_rfe.save()
        if PARTE == 'FPBA':
            PARTE = 'FPBB'
            sitio_hw_control_rfe.homologacion = 'FPBB'
            sitio_hw_control_rfe.save()
        if PARTE == 'J_MR_MA_8MTS_SUPERFLEX':
            PARTE = 'J_MR_MA_8MTS_DCLASS'
            sitio_hw_control_rfe.homologacion = 'J_MR_MA_8MTS_DCLASS'
            sitio_hw_control_rfe.save()
        if PARTE == 'J_HR_MA_4MTS_PREMIUM':
            PARTE = 'J_HR_MA_4MTS_DCLASS'
            sitio_hw_control_rfe.homologacion = 'J_HR_MA_4MTS_DCLASS'
            sitio_hw_control_rfe.save()
        if PARTE == 'FMCF':
            PARTE = 'FMCA'
            sitio_hw_control_rfe.homologacion = 'FMCA'
            sitio_hw_control_rfe.save()
        if PARTE == 'FYTG':
            PARTE = 'FUFAY'
            sitio_hw_control_rfe.homologacion = 'FUFAY'
            sitio_hw_control_rfe.save()
        if PARTE == 'FSFC':
            PARTE = 'FUFAY'
            sitio_hw_control_rfe.homologacion = 'FUFAY'
            sitio_hw_control_rfe.save()
        try:
            asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=PARTE)
            if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr > asignacion_bulk.cantidad * 0.1:            
                sitio_hw_control_rfe.so = asignacion_bulk.so
                sitio_hw_control_rfe.po = asignacion_bulk.po
                sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                sitio_hw_control_rfe.issue_bodega_origen = asignacion_bulk.comentario_bodega
                sitio_hw_control_rfe.save() # termina asignar
                asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                asignacion_bulk.save() # modifica cantidad
        except AsignacionBulk.DoesNotExist:
            pass
    return { 'ok':200 }

