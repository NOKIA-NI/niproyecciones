from django import forms
from django.forms import ModelForm
from .models import (
    FormatoEstacion,
    FormatoParte,
    FormatoClaro,
    FormatoClaroTotal,
    FormatoClaroKit,
    FormatoParteInput,
    FormatoParteDelta,
)

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

class FormatoClaroTotalForm(ModelForm):
    class Meta:
        model = FormatoClaroTotal
        fields = '__all__'

class FilterFormatoClaroTotalForm(ModelForm):

    class Meta:
        model = FormatoClaroTotal
        fields = '__all__'

class FormatoClaroKitForm(ModelForm):
    class Meta:
        model = FormatoClaroKit
        fields = '__all__'

class FilterFormatoClaroKitForm(ModelForm):

    class Meta:
        model = FormatoClaroKit
        fields = '__all__'

class FormatoParteInputForm(ModelForm):
    class Meta:
        model = FormatoParteInput
        fields = '__all__'

class FilterFormatoParteInputForm(ModelForm):
    fecha_formato = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=False)

    class Meta:
        model = FormatoParteInput
        fields = '__all__'

class FormatoParteDeltaForm(ModelForm):
    class Meta:
        model = FormatoParteDelta
        fields = '__all__'

class FilterFormatoParteDeltaForm(ModelForm):
    fecha_formato = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=False)

    class Meta:
        model = FormatoParteDelta
        fields = '__all__'