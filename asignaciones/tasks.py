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
    status_nokia = ['Prueba']
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
    for sitio_hw_control_rfe in sitios_hw_control_rfe:
        if sitio_hw_control_rfe.total_smr == 0: # la necesidad es 0
            sitio_hw_control_rfe.so = 'N/A'
            sitio_hw_control_rfe.po = 'N/A'
            sitio_hw_control_rfe.bodega_origen = 'N/A'
            sitio_hw_control_rfe.save() # termina asignar
        else:
            pos_zina = sitios_pos_zina.filter(site_name=sitio_hw_control_rfe.siteName, parte_capex=sitio_hw_control_rfe.parte ) # filtra por sitio y parte
            if pos_zina.count() == 0: # no hay po en Zina
                count = 0
                try:
                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                    if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                        sitio_hw_control_rfe.so = asignacion_bulk.so
                        sitio_hw_control_rfe.po = asignacion_bulk.po
                        sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                        sitio_hw_control_rfe.save() # termina asignar
                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                        asignacion_bulk.save() # modifica cantidad
                except AsignacionBulk.DoesNotExist:
                    pass
            if pos_zina.count() == 1: # hay una po en zina
                count = 0
                for po_zina in pos_zina:
                    switch = True # switch encendido
                    if sitio_hw_control_rfe.parte == 'J_MR_MA_4MTS_DCLASS'\
                    or sitio_hw_control_rfe.parte == 'J_MR_MA_8MTS_DCLASS'\
                    or sitio_hw_control_rfe.parte == 'J_MR_MA_14MTS_DCLASS':
                        sitio_po = SitioPo.objects.get(numero_po=po_zina.cpo_number)
                        if sitio_po.jumper_status != 'AVAILABLE IN WH': # asignar bulk
                            try:
                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                                if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                    sitio_hw_control_rfe.so = asignacion_bulk.so
                                    sitio_hw_control_rfe.po = asignacion_bulk.po
                                    sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
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
                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                                if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                    sitio_hw_control_rfe.so = asignacion_bulk.so
                                    sitio_hw_control_rfe.po = asignacion_bulk.po
                                    sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                    sitio_hw_control_rfe.save() # termina asignar
                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                    asignacion_bulk.save() # modifica cantidad
                                    switch = False # switch apagado
                            except AsignacionBulk.DoesNotExist:
                                pass
                    if switch: # switch encendido
                        if po_zina.quantity == 0: # asignar bulk
                            try:
                                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                                if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                    sitio_hw_control_rfe.so = asignacion_bulk.so
                                    sitio_hw_control_rfe.po = asignacion_bulk.po
                                    sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                    sitio_hw_control_rfe.save() # termina asignar
                                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                    asignacion_bulk.save() # modifica cantidad
                            except AsignacionBulk.DoesNotExist:
                                pass
                        if po_zina.quantity > 0: # asignar
                            if po_zina.quantity - sitio_hw_control_rfe.total_smr >= 0: # asignar po
                                sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                if sitio_hw_control_rfe.parte == 'J_MR_MA_4MTS_DCLASS'\
                                or sitio_hw_control_rfe.parte == 'J_MR_MA_8MTS_DCLASS'\
                                or sitio_hw_control_rfe.parte == 'J_MR_MA_14MTS_DCLASS':
                                    sitio_hw_control_rfe.so = sitio_po.jumper
                                else:
                                    sitio_hw_control_rfe.so = sitio_po.bts
                                sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                                sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                sitio_hw_control_rfe.save() # termina asignar
                                po_zina.quantity = po_zina.quantity - sitio_hw_control_rfe.total_smr
                                po_zina.save() # modifica quantity
                            else:
                                count = po_zina.quantity
                                sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                if sitio_hw_control_rfe.parte == 'J_MR_MA_4MTS_DCLASS'\
                                or sitio_hw_control_rfe.parte == 'J_MR_MA_8MTS_DCLASS'\
                                or sitio_hw_control_rfe.parte == 'J_MR_MA_14MTS_DCLASS':
                                    sitio_hw_control_rfe.so = sitio_po.jumper
                                else:
                                    sitio_hw_control_rfe.so = sitio_po.bts
                                sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(po_zina.quantity)
                                sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                                sitio_hw_control_rfe.save() # termina asignar
                                po_zina.quantity -= po_zina.quantity
                                po_zina.save() # modifica quantity
                                try:
                                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
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
                    if sitio_hw_control_rfe.parte == 'J_MR_MA_4MTS_DCLASS'\
                    or sitio_hw_control_rfe.parte == 'J_MR_MA_8MTS_DCLASS'\
                    or sitio_hw_control_rfe.parte == 'J_MR_MA_14MTS_DCLASS':
                        sitio_po = SitioPo.objects.get(numero_po=po_zina.cpo_number)
                        if sitio_po.jumper_status != 'AVAILABLE IN WH': # asignar bulk
                            switch = False # switch apagado
                    if sitio_hw_control_rfe == 'FXCB':
                        sitio_po = SitioPo.objects.get(numero_po=po_zina.cpo_number)
                        if sitio_po.fxcb == 'FXCB separated' and sitio_po.fxcb_status != 'AVAILABLE IN WH': # asignar bulk
                            switch = False # switch apagado
                    if switch: # switch encendido
                        if po_zina.quantity > 0: # asignar
                            if (po_zina.quantity - sitio_hw_control_rfe.total_smr) + count >= 0: # asignar po
                                if count > 0:
                                    sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                    if sitio_hw_control_rfe.parte == 'J_MR_MA_4MTS_DCLASS'\
                                    or sitio_hw_control_rfe.parte == 'J_MR_MA_8MTS_DCLASS'\
                                    or sitio_hw_control_rfe.parte == 'J_MR_MA_14MTS_DCLASS':
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
                                if count > 0:
                                    count += po_zina.quantity
                                    sitio_po = sitios_po.get(numero_po=po_zina.cpo_number)
                                    if sitio_hw_control_rfe.parte == 'J_MR_MA_4MTS_DCLASS'\
                                    or sitio_hw_control_rfe.parte == 'J_MR_MA_8MTS_DCLASS'\
                                    or sitio_hw_control_rfe.parte == 'J_MR_MA_14MTS_DCLASS':
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
                                    if sitio_hw_control_rfe.parte == 'J_MR_MA_4MTS_DCLASS'\
                                    or sitio_hw_control_rfe.parte == 'J_MR_MA_8MTS_DCLASS'\
                                    or sitio_hw_control_rfe.parte == 'J_MR_MA_14MTS_DCLASS':
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
                        asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                        if (asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr) + count > asignacion_bulk.cantidad * 0.1:
                            sitio_hw_control_rfe.issue_bodega_origen = 'FaltanteX' + str(sitio_hw_control_rfe.total_smr - count) + ' ' + asignacion_bulk.po + ' ' + asignacion_bulk.bodega  
                            sitio_hw_control_rfe.save() # termina asignar
                            asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                            asignacion_bulk.save() # modifica cantidad
                    except AsignacionBulk.DoesNotExist:
                        pass
                if count == 0: # asignar bulk
                        try:
                            asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                            if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                                sitio_hw_control_rfe.so = asignacion_bulk.so
                                sitio_hw_control_rfe.po = asignacion_bulk.po
                                sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                                sitio_hw_control_rfe.save() # termina asignar
                                asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                                asignacion_bulk.save() # modifica cantidad
                        except AsignacionBulk.DoesNotExist:
                            pass
    sitios_pos_zina = sitios_pos_zina.filter(quantity__gt=0) # sobrantes
    for sitio_po_zina in sitios_pos_zina:
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
    return { 'ok':200 }

@shared_task
def task_asignacion_bulk():
    current_task.update_state(state='PROGRESS')
    sitios_bulk = SitioBulk.objects.all()
    list_site_name = [ sitio.estacion.site_name for sitio in sitios_bulk ]
    sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__in=list_site_name) # filtra sitios bilk en rfe
    for sitio_hw_control_rfe in sitios_hw_control_rfe:
        try:
            asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
            if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr > asignacion_bulk.cantidad * 0.1:            
                sitio_hw_control_rfe.so = asignacion_bulk.so
                sitio_hw_control_rfe.po = asignacion_bulk.po
                sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                sitio_hw_control_rfe.save() # termina asignar
                asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                asignacion_bulk.save() # modifica cantidad
        except AsignacionBulk.DoesNotExist:
            pass
    return { 'ok':200 }

