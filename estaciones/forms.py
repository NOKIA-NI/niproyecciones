from django import forms
from django.forms import ModelForm
from .models import Estacion, BitacoraEstacion, ProyeccionEstacion
from . import choices

# REGION_CHOICES_EMPTY = (('', '---------'),) + choices.REGION_CHOICES

class EstacionForm(ModelForm):
    class Meta:
        model = Estacion
        fields = '__all__'

class FilterEstacionForm(ModelForm):
    # site_name = forms.CharField(required=False)
    # region = forms.ChoiceField(choices=REGION_CHOICES_EMPTY, required=False)

    class Meta:
        model = Estacion
        fields = '__all__'

class BitacoraEstacionForm(ModelForm):
    estacion = forms.ModelChoiceField(queryset=Estacion.objects.all())
    fecha_bitacora = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    observaciones = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = BitacoraEstacion
        fields = '__all__'

class FilterBitacoraEstacionForm(ModelForm):
    fecha_bitacora = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=False)

    class Meta:
        model = BitacoraEstacion
        fields = '__all__'

class ProyeccionEstacionForm(ModelForm):

    class Meta:
        model = ProyeccionEstacion
        fields = '__all__'

class FilterProyeccionEstacionForm(ModelForm):
    fecha_proyeccion = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=False)

    class Meta:
        model = ProyeccionEstacion
        fields = '__all__'

