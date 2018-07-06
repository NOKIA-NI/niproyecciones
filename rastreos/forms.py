from django import forms
from django.forms import ModelForm
from .models import Rastreo, Proceso
from users.models import Perfil
from . import choices
from django.core.mail import send_mail

ESTADO_PROCESO_CHOICES_EMPTY = (('', '---------'),) + choices.ESTADO_PROCESO_CHOICES

ABIERTO = 'Abierto'
CERRADO = 'Cerrado'
GRUPOHW = 'Grupo HW'
MBB = 'MBB'
TCC = 'TCC'
MBBOFFERTS = 'MBB Offerts'
FYC = 'F&C'
LOGISTICA = 'Logistica'
FACTORY = 'Factory'

class RastreoForm(ModelForm):
    class Meta:
        model = Rastreo
        fields = '__all__'

class FilterRastreoForm(ModelForm):

    class Meta:
        model = Rastreo
        fields = '__all__'

class ProcesoForm(ModelForm):
    # archivo = forms.FileField(required=True)
    class Meta:
        model = Proceso
        fields = '__all__'

    def clean(self):
        cleaned_data = super(ProcesoForm, self).clean()
        estado_proceso = cleaned_data.get('estado_proceso')
        tipo_proceso = self.instance.tipo_proceso
        rastreo = self.instance.rastreo

        if estado_proceso == CERRADO and tipo_proceso == GRUPOHW:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=MBB
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == MBB:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=TCC
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == TCC:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=MBBOFFERTS
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == MBBOFFERTS:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=FYC
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == FYC:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=LOGISTICA
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == LOGISTICA:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=FACTORY
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        
        return cleaned_data

class FilterProcesoForm(ModelForm):
    estado_proceso = forms.ChoiceField(choices=ESTADO_PROCESO_CHOICES_EMPTY, required=False)

    class Meta:
        model = Proceso
        fields = ('rastreo', 'responsable', 'tipo_proceso', 'estado_proceso')

class PerfilProcesoForm(ModelForm):
    estado_proceso = forms.ChoiceField(choices=ESTADO_PROCESO_CHOICES_EMPTY, required=True)
    comentario = forms.CharField(widget=forms.Textarea(), required=True)
    archivo = forms.FileField(required=True)

    class Meta:
        model = Proceso
        fields = ('estado_proceso', 'comentario', 'archivo')

    def clean(self):
        print(self.instance.tipo_proceso)
        cleaned_data = super(PerfilProcesoForm, self).clean()
        estado_proceso = cleaned_data.get('estado_proceso')
        tipo_proceso = self.instance.tipo_proceso
        rastreo = self.instance.rastreo

        if (estado_proceso == CERRADO):
            pass
        else:
            raise forms.ValidationError('El estado del proceso debe ser Cerrado.')

        if estado_proceso == CERRADO and tipo_proceso == GRUPOHW:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=MBB
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == MBB:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=TCC
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == TCC:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=MBBOFFERTS
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == MBBOFFERTS:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=FYC
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == FYC:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=LOGISTICA
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        if estado_proceso == CERRADO and tipo_proceso == LOGISTICA:
            proceso = Proceso.objects.create(
                rastreo=rastreo,
                responsable=Perfil.objects.get(id=1),
                tipo_proceso=FACTORY
            )
            send_mail(
            proceso.tipo_proceso,
            'Este correo es para el proceso ' + proceso.tipo_proceso,
            'notificaciones@nihardware.com',
            [proceso.responsable.email],
            fail_silently=False,
            )
        
        return cleaned_data