from django.contrib import admin

from .models import Curso
from .models import Directivo
from .models import Preceptor
from .models import Alumno
from .models import PadreTutor
from .models import Formulario
from .models import SolicitudReunion
from .models import Comunicado
from .models import ComunicadoRecibido
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group


User = get_user_model()


# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
         queryset=User.objects.all(),
         required=False,
         # Use the pretty 'filter_horizontal widget'.
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance

admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_padre','is_staff', 'is_active',)
    list_filter = ('username', 'is_padre','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ( 'is_padre','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_padre','is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)



# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Curso, CursoAdmin)

class DirectivoAdmin(admin.ModelAdmin):
    model = Directivo
    list_display = ('id','first_name','last_name','email','username','cargo')

    search_fields = (
        'first_name','last_name','cargo'
    )

admin.site.register(Directivo,DirectivoAdmin)

class PreceptorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Preceptor,PreceptorAdmin)

class AlumnoAdmin(admin.ModelAdmin):
    model = Alumno
    list_display = ('id','first_name','last_name','curso','dni','tutor')

    search_fields = (
        'first_name','last_name',
    )
admin.site.register(Alumno,AlumnoAdmin)

class PadreTutorAdmin(admin.ModelAdmin):
    model = Comunicado
    list_display = ('id','first_name','last_name','email','user','delegado')

    search_fields = (
        'first_name','last_name','delegado'
    )
admin.site.register(PadreTutor,PadreTutorAdmin)


class FormularioAdmin(admin.ModelAdmin):
    model = Formulario
    list_display = ('id','alumno','tipo_form','fecha')

    search_fields = (
        'alumno','tipo_form','fecha'
    )

admin.site.register(Formulario,FormularioAdmin)

class SolicitudReunionAdmin(admin.ModelAdmin):
    model = SolicitudReunion
    list_display = ('id','padre','fecha')

    search_fields = (
        'padre','fecha'
    )

admin.site.register(SolicitudReunion,SolicitudReunionAdmin)

class ComunicadoAdmin(admin.ModelAdmin):
    model = Comunicado
    list_display = ('id','titulo','fecha','directivo','curso')

    search_fields = (
        'titulo','fecha','directivo','curso'
    )

admin.site.register(Comunicado,ComunicadoAdmin)

class ComunicadoRecibidoAdmin(admin.ModelAdmin):
    pass

admin.site.register(ComunicadoRecibido,ComunicadoRecibidoAdmin)
