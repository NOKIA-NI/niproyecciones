from django import forms
from django.forms import ModelForm
from .models import Tarea, GrupoTarea

class GrupoTareaForm(ModelForm):
    
    class Meta:
        model = GrupoTarea
        fields = '__all__'

class FilterGrupoTareaForm(ModelForm):
    nombre = forms.CharField(required=False)
    
    class Meta:
        model = GrupoTarea
        fields = ('nombre',)

class TareaForm(ModelForm):

    class Meta:
        model = Tarea
        fields = '__all__'

class FilterTareaForm(ModelForm):
    nombre = forms.CharField(required=False)
    
    class Meta:
        model = Tarea
        fields = ('nombre', 'grupo_tarea')
