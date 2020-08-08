from django.db import models
import datetime

# Create your models here.
class Directivo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Comunicado(models.Model):
    fecha = models.dateField()
    remitente = models.CharField(max_length=30)
    directivo = models.ForeignKey(Directivo,on_delete=models.CASCADE)
    mensaje = models.TextField()
