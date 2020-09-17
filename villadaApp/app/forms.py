from django import forms
from .models import Comunicado
from django.contrib.admin import widgets

class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado

        fields = [
        'titulo',
        'fecha',
        'directivo',
        'mensaje',
        'curso',
        ]
        labels = {
        'titulo': 'Titulo',
        'fecha': 'Fecha',
        'directivo': 'Directivo',
        'mensaje':'Mensaje',
        'curso':'Cursos',
        }
        widgets = {
        'titulo': forms.TextInput(attrs={'class':'form-control'}),
        'fecha': forms.TextInput(attrs={'class':'form-control'}),
        'directivo': forms.Select(attrs={'class':'form-control'}),
        'mensaje':forms.Textarea(attrs={'class':'form-control'}),
        'curso':forms.CheckboxSelectMultiple(),
        }
