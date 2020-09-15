from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
# Create your models here.
class Curso(models.Model):

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

    curso = models.CharField(max_length=2, choices=Cursos.choices, default=Cursos.primeroA)

class Directivo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Preceptor(models.Model):
    curso = models.ManyToManyField(Curso)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)

class Alumno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)

class PadreTutor(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    delegado = models.BooleanField(default=False)

class Formulario(models.Model):

    class TipoForm(models.TextChoices):
        F1 = 'F1', ('Formulario 1')
        F2 = 'F2', ('Formulario 2')
        F3 = 'F3', ('Formulario 3')

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tipo_form = models.CharField(max_length=2, choices=TipoForm.choices, default=TipoForm.F1)

class SolicitudReunion(models.Model):
    #Se debe agregar un estado de reunion(Aceptada, denegada, Procesando)

    padre = models.ForeignKey(PadreTutor, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.TextField()

class ComunicadoCurso(models.Model):
    titulo = models.CharField(max_length=500, null=True, blank=True)
    fecha = models.DateField()
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField()
    cursos = models.ManyToManyField(Curso)

class ComunicadoCiclo(models.Model):
    titulo = models.CharField(max_length=500, null=True, blank=True)
    CICLOS = (
    ("B", "Basico"),
    ("A", "Avanzado"),
)
    fecha = models.DateField()
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField()
    ciclo = models.CharField(max_length = 20 ,choices = CICLOS, default = 'B')

class ComunicadoGeneral(models.Model):
    titulo = models.CharField(max_length=500, null=True, blank=True)
    fecha = models.DateField()
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField()
