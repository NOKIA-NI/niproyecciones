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
    status_nokia = ['Complete Sites (Installed)', 'Parcial FXCB', 'Parcial Jumpers', 'Complete Sites (Por Armar LSM)']
    sitios_asignacion = HwSiteList.objects.filter(status_nokia__in=status_nokia, solicitud_hw='1', estado_HW='NO CONFIRMADO')
    Bolsa_HW = ['Sitios Bulk', 'LSM A BULK']
    sitios_asignacion_bolsa = sitios_asignacion.exclude(Bolsa_HW=Bolsa_HW)
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
    po_zina = PoZina.objects.all()
    sitios_po = po_zina.filter(site_name__in=list_site_name).order_by('site_name').distinct('site_name')
    list_po_zina = [ po_zina.cpo_number for po_zina in sitios_po ]
    estados_po = EstadoPo.objects.filter(numero_po__in=list_po_zina)

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

    sitios_po = SitioPo.objects.filter(bts_status='AVAILABLE IN WH')
    list_sitio_po = [sitio_po.numero_po for sitio_po in sitios_po ]

    pos_zina = PoZina.objects.filter(cpo_number__in=list_sitio_po) # filtra por po's AVAILABLE IN WH
    list_site_name = [ sitio.site_name for sitio in pos_zina ]
    list_site_name = list(set(list_site_name))

    sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__in=list_site_name) # sitios filtro rfe

    for sitio_hw_control_rfe in sitios_hw_control_rfe:

        if sitio_hw_control_rfe.total_smr == 0:

            sitio_hw_control_rfe.so = 'N/A'
            sitio_hw_control_rfe.po = 'N/A'
            sitio_hw_control_rfe.bodega_origen = 'N/A'
            # sitio_hw_control_rfe.save() # termina asignar
            break

        po_zina = pos_zina.filter(site_name=sitio_hw_control_rfe.siteName, parte_capex=sitio_hw_control_rfe.parte ) # filtra por sitio y parte

        if po_zina.count() == 0: # no hay la parte en Zina
            asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
            if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                
                sitio_hw_control_rfe.so = asignacion_bulk.so
                sitio_hw_control_rfe.po = asignacion_bulk.po
                sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                # sitio_hw_control_rfe.save() # termina asignar
                asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                # asignacion_bulk.save() # modifica cantidad

        if po_zina.count() > 1: # dos po
            count = 0
            for pz in po_zina:

                if pz.quantity > 0: # asignar

                    if pz.quantity - sitio_hw_control_rfe.total_smr + count >= 0: # asignar po

                        if count > 0:
                            sitio_po = sitios_po.get(numero_po=pz.cpo_number)
                            sitio_hw_control_rfe.so = str(sitio_hw_control_rfe.so) + '+' + str(sitio_po.bts)
                            sitio_hw_control_rfe.po = str(sitio_hw_control_rfe.po) + '+' + str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                            sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                            # sitio_hw_control_rfe.save() # termina asignar
                            pz.quantity = pz.quantity - sitio_hw_control_rfe.total_smr
                            # pz.quantity.save() # modifica quantity
                            count = 0
                            break

                        sitio_po = sitios_po.get(numero_po=pz.cpo_number)
                        sitio_hw_control_rfe.so = sitio_po.bts
                        sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                        sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                        # sitio_hw_control_rfe.save() # termina asignar
                        pz.quantity = pz.quantity - sitio_hw_control_rfe.total_smr
                        # pz.quantity.save() # modifica quantity
                        count = 0
                        break

                    if pz.quantity - sitio_hw_control_rfe.total_smr + count < 0: # asignar po

                        if count > 0:

                            count += pz.quantity

                            sitio_po = sitios_po.get(numero_po=pz.cpo_number)

                            sitio_hw_control_rfe.so = str(sitio_hw_control_rfe.so) + '+' + str(sitio_po.bts)
                            sitio_hw_control_rfe.po = str(sitio_hw_control_rfe.po) + '+' + str(sitio_po.numero_po) + 'X' + str(pz.quantity)
                            sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                            # sitio_hw_control_rfe.save() # termina asignar
                            pz.quantity -= pz.quantity
                            # pz.quantity.save() # modifica quantity

                        if count == 0:

                            count += pz.quantity

                            sitio_po = sitios_po.get(numero_po=pz.cpo_number)

                            sitio_hw_control_rfe.so = sitio_po.bts
                            sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(pz.quantity)
                            sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                            # sitio_hw_control_rfe.save() # termina asignar
                            pz.quantity -= pz.quantity
                            # pz.quantity.save() # modifica quantity

            if count > 0: # asignar bulk

                asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)

                if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:

                    sitio_hw_control_rfe.issue_bodega_origen = 'FaltanteX' + str(sitio_hw_control_rfe.total_smr - count) + ' Bulk ' + asignacion_bulk.bodega  
                    # sitio_hw_control_rfe.save() # termina asignar
                    asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                    # asignacion_bulk.save() # modifica cantidad

            if count == 0: # asignar bulk

                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                    if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr  + count > asignacion_bulk.cantidad * 0.1:
                        
                        sitio_hw_control_rfe.so = asignacion_bulk.so
                        sitio_hw_control_rfe.po = asignacion_bulk.po
                        sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                        # sitio_hw_control_rfe.save() # termina asignar
                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                        # asignacion_bulk.save() # modifica cantidad
                
        if po_zina.count() == 1: # una po
            count = 0
            for pz in po_zina:

                if pz.quantity == 0: # asignar bulk

                    asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)
                    if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr  + count > asignacion_bulk.cantidad * 0.1:
                        
                        sitio_hw_control_rfe.so = asignacion_bulk.so
                        sitio_hw_control_rfe.po = asignacion_bulk.po
                        sitio_hw_control_rfe.bodega_origen = asignacion_bulk.bodega
                        # sitio_hw_control_rfe.save() # termina asignar
                        asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                        # asignacion_bulk.save() # modifica cantidad

                if pz.quantity > 0: # asignar

                    if pz.quantity - sitio_hw_control_rfe.total_smr >= 0: # asignar po

                        sitio_po = sitios_po.get(numero_po=pz.cpo_number)

                        sitio_hw_control_rfe.so = sitio_po.bts
                        sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(sitio_hw_control_rfe.total_smr)
                        sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                        # sitio_hw_control_rfe.save() # termina asignar
                        pz.quantity = pz.quantity - sitio_hw_control_rfe.total_smr
                        # pz.quantity.save() # modifica quantity

                    if pz.quantity - sitio_hw_control_rfe.total_smr < 0: # asignar po + bulk

                        count = pz.quantity

                        sitio_po = sitios_po.get(numero_po=pz.cpo_number)

                        sitio_hw_control_rfe.so = sitio_po.bts
                        sitio_hw_control_rfe.po = str(sitio_po.numero_po) + 'X' + str(pz.quantity)
                        sitio_hw_control_rfe.bodega_origen = 'Panalpina'
                        # sitio_hw_control_rfe.save() # termina asignar
                        pz.quantity -= pz.quantity
                        # pz.quantity.save() # modifica quantity

                        asignacion_bulk = AsignacionBulk.objects.get(parte__parte_nokia=sitio_hw_control_rfe.parte)

                        if asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr + count > asignacion_bulk.cantidad * 0.1:
                            
                            sitio_hw_control_rfe.issue_bodega_origen = 'FaltanteX' + str(sitio_hw_control_rfe.total_smr - count) + ' Bulk ' + asignacion_bulk.bodega  
                            # sitio_hw_control_rfe.save() # termina asignar
                            asignacion_bulk.cantidad = asignacion_bulk.cantidad - sitio_hw_control_rfe.total_smr
                            # asignacion_bulk.save() # modifica cantidad

    pos_zina = pos_zina.filter(quantity__gt=0) # sobrantes

    for po_zina in pos_zina:
        sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__iexact=po_zina.site_name, parte=po_zina.parte_capex) # sitios filtro rfe

        if sitios_hw_control_rfe.count() > 0:
            for sitio_hw_control_rfe in sitios_hw_control_rfe:
                if sitio_hw_control_rfe.total_smr > 0:
                    if po_zina.quantity < 10:
                        sitio_hw_control_rfe.material_sobrante += '00' + str(po_zina.quantity) + 'X' + po_zina.parte_capex + 'X' + str(po_zina.cpo_number) + ','
                    if po_zina.quantity >= 10 and po_zina.quantity < 100:
                        sitio_hw_control_rfe.material_sobrante += '0' + str(po_zina.quantity) + 'X' + po_zina.parte_capex + 'X' + str(po_zina.cpo_number) + ','
                    if po_zina.quantity >= 100:
                        sitio_hw_control_rfe.material_sobrante += str(po_zina.quantity) + 'X' + po_zina.parte_capex + 'X' + str(po_zina.cpo_number) + ','
                    break
        else:
            sitios_hw_control_rfe = HwControlRfe.objects.filter(siteName__iexact=po_zina.site_name)
            for sitio_hw_control_rfe in sitios_hw_control_rfe:
                if sitio_hw_control_rfe.total_smr > 0:
                    if po_zina.quantity < 10:
                        sitio_hw_control_rfe.material_sobrante += '00' + str(po_zina.quantity) + 'X' + po_zina.parte_capex + 'X' + str(po_zina.cpo_number) + ','
                    if po_zina.quantity >= 10 and po_zina.quantity < 100:
                        sitio_hw_control_rfe.material_sobrante += '0' + str(po_zina.quantity) + 'X' + po_zina.parte_capex + 'X' + str(po_zina.cpo_number) + ','
                    if po_zina.quantity >= 100:
                        sitio_hw_control_rfe.material_sobrante += str(po_zina.quantity) + 'X' + po_zina.parte_capex + 'X' + str(po_zina.cpo_number) + ','
                    break

    return { 'ok':200 }

@shared_task
def task_asignacion_bulk():
    current_task.update_state(state='PROGRESS')
    return { 'ok':200 }

