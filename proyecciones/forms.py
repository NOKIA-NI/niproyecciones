from django import forms
from django.forms import ModelForm
from .models import Proyeccion, ProyeccionExtra

class ProyeccionForm(ModelForm):
    class Meta:
        model = Proyeccion
        fields = '__all__'

class FilterProyeccionForm(ModelForm):
    id = forms.IntegerField(required=False)
    
    class Meta:
        model = Proyeccion
        fields = '__all__'

class ProyeccionExtraForm(ModelForm):
    class Meta:
        model = ProyeccionExtra
        fields = '__all__'

class FilterProyeccionExtraForm(ModelForm):
    id = forms.IntegerField(required=False)
    
    class Meta:
        model = ProyeccionExtra
        fields = '__all__'
