from django.db import models
import datetime
from django import forms
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from django.contrib.auth.models import Group

# Create your models here.
# Create your models here.
class Curso(models.Model):
    title = models.CharField(max_length=30)
    #general = ('1A', ('Primero A'), '1B', ('Primero B'), '1C', ('Primero C'))
    class Cursos(models.TextChoices):
        primeroA = '1A', ('Primero A')
        primeroB = '1B', ('Primero B')
        primeroC = '1C', ('Primero C')

        segundoA = '2A', ('Segundo A')
        segundoB = '2B', ('Segundo B')
        segundoC = '2C', ('Segundo C')

        terceroA = '3A', ('Tercero A')
        terceroB = '3B', ('Tercero B')
        terceroC = '3C', ('Tercero C')

        cuartoA = '4A', ('Cuarto A')
        cuartoB = '4B', ('Cuarto B')
        cuartoC = '4C', ('Cuarto C')

        quintoA = '5A', ('Quinto A')
        quintoB = '5B', ('Quinto B')
        quintoC = '5C', ('Quinto C')

        sextoA = '6A', ('Sexto A')
        sextoB = '6B', ('Sexto B')
        sextoC = '6C', ('Sexto C')

        septimoA = '7A', ('Septimo A')
        septimoB = '7B', ('Septimo B')
        septimoC = '7C', ('Septimo C')

    def __str__(self):
        return self.title

class Directivo(models.Model):
    CARGO_CHOICES = [
    ('DG', 'Director General'),
    ('DA', 'Director Academico'),
    ('VD', 'Vicedirector'),
]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    cargo=models.CharField(max_length=2,choices=CARGO_CHOICES, default='VD')

    def __str__(self):
        return (self.first_name + " "+ self.last_name)

    def save(self, *args, **kwargs):
        if self.cargo=='DA':
            obj=Directivo.objects.filter(cargo='DA')
            if obj.exists():
                raise ValidationError('Solo puede existir un Directivo Academico',code='invalid')
            else:
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


class Preceptor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    curso = MultiSelectField(choices=Curso.Cursos.choices, null=True, blank=True)



    def __str__(self):
        return (self.first_name + " "+ self.last_name)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(_('email address'))
    is_padre = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class PadreTutor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    delegado = models.BooleanField(default=False)

    def __str__(self):
        return (self.first_name + " "+ self.last_name)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
	
    my_group, exist = Group.objects.get_or_create(name='Padres') 
	
    if created:
        #print(instance)
        if instance.is_padre:
            my_group.user_set.add(instance)
        PadreTutor.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
        Token.objects.create(user=instance)



class Alumno(models.Model):
    curso = models.CharField(max_length=2, choices=Curso.Cursos.choices)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    tutor = models.ForeignKey(PadreTutor, on_delete=models.CASCADE)

    def __str__(self):
        return (self.first_name + " "+ self.last_name)



class Formulario(models.Model):

    class TipoForm(models.TextChoices):
        F1 = 'F1', ('Formulario 1')
        F2 = 'F2', ('Formulario 2')
        F3 = 'F3', ('Formulario 3')

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tipo_form = models.CharField(max_length=2, choices=TipoForm.choices, default=TipoForm.F1)
    dias=models.CharField(max_length=45, null=True)
    fecha=models.DateField()
    hora= models.CharField(max_length=45, null=True)

    def __str__(self):
        return ("Alumno: "+str(self.alumno))


    def save(self, *args, **kwargs):
        txt=''
        if self.tipo_form=='F1':
            txt= 'Córdoba, '+str(self.fecha)+'.\n Prof. '+str(Directivo.objects.get(cargo='DA'))+' \nMe dirijo a Ud. a los efectos de solicitarle la justificación de la/s inasistencia/s del Alumno '+str(self.alumno)+' del curso: '+str(self.alumno.curso)+' debido a: '+str(self.descripcion)+' los dias: '+str(self.dias)
        elif self.tipo_form=='F2':
            txt= 'Córdoba, '+str(self.fecha)+'.\n Prof. '+str(Directivo.objects.get(cargo='DA'))+' \nMe dirijo a Ud. a los efectos de autorizar, en el día de la fecha , al Alumno '+str(self.alumno)+' del curso: '+str(self.alumno.curso)+'a retirarse del Establecimiento por sus propios medios, por ausencia del docente, u otra causa imprevista que pudiere surgir. Sin otro particular le saludo atte. '
        else:
            txt='Córdoba, '+str(self.fecha)+'.\n Prof. '+str(Directivo.objects.get(cargo='DA'))+' \nMe dirijo a Ud. a los efectos de autorizar, en el día de la fecha , al Alumno '+str(self.alumno)+' del curso: '+str(self.alumno.curso)+'a retirarse del Establecimiento por sus propios medios,'+str(self.alumno)+' del curso: '+str(self.alumno.curso)+' a las '+ str(self.hora)+'hs debido a: '+str(self.descripcion)
        self.descripcion = txt
        super().save(*args, **kwargs)

class SolicitudReunion(models.Model):
    #Se debe agregar un estado de reunion(Aceptada, denegada, Procesando)
    padre = models.ForeignKey(PadreTutor, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.TextField()

    def __str__(self):
        return ("Solicitante: "+self.padre)

class Comunicado(models.Model):
    titulo = models.CharField(max_length=500, null=True, blank=True)
    fecha = models.DateField()
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField()
    #curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    curso = MultiSelectField(choices=Curso.Cursos.choices)
    def __str__(self):
        return (self.titulo)
'''director general=ramacciotti
director academico=adriana
Vicedirectores=ruben y pablo'''
