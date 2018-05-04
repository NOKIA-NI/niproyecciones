from django import forms
from django.forms import ModelForm
from .models import Proyeccion

class ProyeccionForm(ModelForm):
    class Meta:
        model = Proyeccion
        fields = '__all__'

class FilterProyeccionForm(ModelForm):
    id = forms.IntegerField(required=False)
    
    class Meta:
        model = Proyeccion
        fields = '__all__'
