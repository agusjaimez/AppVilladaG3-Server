from django import forms
from .models import Comunicado
from django.contrib.admin import widgets

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',  'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',  'email')
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        ]
        labels = {
        'username': 'Usuario',
        'first_name': 'Nombre',
        'last_name': 'Apellido',
        'email':'Email',
        }
        widgets = {
        'username': forms.TextInput(attrs={'class':'form-control'}),
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'last_name': forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        }

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
