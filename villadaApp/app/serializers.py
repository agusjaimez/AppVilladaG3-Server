from rest_framework import serializers

from .models import Comunicado, Directivo, PadreTutor, Alumno, Directivo


class DirectivoSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Directivo
        fields = ('first_name', 'last_name', 'username', 'email', 'cargo')

class ComunicadoSer(serializers.HyperlinkedModelSerializer):
    directivo = DirectivoSer()
    class Meta:
        model = Comunicado
        fields = ('titulo', 'fecha', 'curso', 'directivo', 'mensaje',)

class PadreSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PadreTutor
        fields = ('first_name', 'last_name', 'username')

class AlumnoSer(serializers.HyperlinkedModelSerializer):
    tutor = PadreSer()
    class Meta:
        model = Alumno
        fields = ('first_name', 'last_name', 'dni', 'tutor')
