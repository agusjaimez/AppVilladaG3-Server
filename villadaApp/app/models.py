from django.db import models
import datetime

# Create your models here.
class Curso(models.Model):

    class Cursos(models.TextChoices):
        primeroA = '1A', _('Primero A')
        primeroB = '1B', _('Primero B')
        primeroC = '1C', _('Primero C')

        segundoA = '2A', _('Segundo A')
        segundoB = '2B', _('Segundo B')
        segundoC = '2C', _('Segundo C')

        terceroA = '3A', _('Tercero A')
        terceroB = '3B', _('Tercero B')
        terceroC = '3C', _('Tercero C')

        cuartoA = '4A', _('Cuarto A')
        cuartoB = '4B', _('Cuarto B')
        cuartoC = '4C', _('Cuarto C')

        quintoA = '5A', _('Quinto A')
        quintoB = '5B', _('Quinto B')
        quintoC = '5C', _('Quinto C')

        sextoA = '6A', _('Sexto A')
        sextoB = '6B', _('Sexto B')
        sextoC = '6C', _('Sexto C')

        septimoA = '7A', _('Septimo A')
        septimoB = '7B', _('Septimo B')
        septimoC = '7C', _('Septimo C')

    curso = models.CharField(max_length=2, choices=Cursos.choices, default=Cursos.primeroA)

class Directivo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Preceptor(models.Model):
    curso = models.ManyToManyField(Curso, on_delete=models.SET_NULL)
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
        F1 = 'F1', _('Formulario 1')
        F2 = 'F2', _('Formulario 2')
        F3 = 'F3', _('Formulario 3')

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    descripcion = models.TextField()
    tipo_form = models.CharField(max_length=2, choices=TipoForm.choices, default=TipoForm.F1)

class SolicitudReunion(models.Model):
    #Se debe agregar un estado de reunion(Aceptada, denegada, Procesando)
    padre = models.ForeignKey(PadreTutor, on_delete=models.CASCADE)
    fecha = models.dateField()
    motivo = models.TextField()

class ComunicadoCurso(models.Model):
    fecha = models.dateField()
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE)
    mensaje = models.TextField()
    cursos = models.ManyToManyField(Curso)

class ComunicadoCiclo(models.Model):
    CICLOS = (
    ("B", "Basico"),
    ("A", "Avanzado"),
)
    fecha = models.dateField()
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE)
    mensaje = models.TextField()
    ciclo = models.CharField(max_length = 20 ,choices = CICLOS, default = 'B')

class ComunicadoGeneral(models.Model):
    fecha = models.dateField()
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE)
    mensaje = models.TextField()
