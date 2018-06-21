from django import forms
from django.forms import ModelForm
from .models import FormatoEstacion, FormatoParte, FormatoClaro

class FormatoEstacionForm(ModelForm):
    class Meta:
        model = FormatoEstacion
        fields = '__all__'

class FilterFormatoEstacionForm(ModelForm):

    class Meta:
        model = FormatoEstacion
        fields = '__all__'

class FormatoParteForm(ModelForm):
    class Meta:
        model = FormatoParte
        fields = '__all__'

class FilterFormatoParteForm(ModelForm):

    class Meta:
        model = FormatoParte
        fields = '__all__'

class FormatoClaroForm(ModelForm):
    class Meta:
        model = FormatoClaro
        fields = '__all__'

class FilterFormatoClaroForm(ModelForm):

    class Meta:
        model = FormatoClaro
        fields = '__all__'