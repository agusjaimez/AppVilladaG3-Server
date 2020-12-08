from rest_framework import serializers
from .models import Comunicado, Directivo, PadreTutor, Alumno, Directivo, Formulario, ComunicadoRecibido
#from django.contrib.auth.models import User
from .models import CustomUser as User
from rest_framework.validators import UniqueTogetherValidator

class DirectivoSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Directivo
        fields = ('first_name', 'last_name', 'username', 'email', 'cargo')

class ComunicadoSer(serializers.HyperlinkedModelSerializer):
    directivo = DirectivoSer()
    class Meta:
        model = Comunicado
        fields = ('id','titulo', 'fecha', 'curso', 'directivo', 'mensaje')

class PadreSer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PadreTutor
        fields = ('first_name', 'last_name', 'username')

class AlumnoSer(serializers.HyperlinkedModelSerializer):
    tutor = PadreSer()
    class Meta:
        model = Alumno
        fields = ('first_name', 'last_name', 'curso','dni', 'tutor')

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

class AlumnooSer(serializers.ModelSerializer):

    def create(self, validated_data):
        alumno = Alumno.objects.create_user()
        return alumno

    class Meta:
        model = Alumno
        fields = (
            'id',
            'curso',
            'first_name',
            'last_name',
            'dni',
            'tutor',
        )

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ('alumno', 'descripcion', 'tipo_form', 'dias', 'fecha', 'hora')


class ComunicadoRecibidoSer(serializers.ModelSerializer):

    class Meta:
        model = ComunicadoRecibido
        fields = (
            'id',
            'recibido'
        )
