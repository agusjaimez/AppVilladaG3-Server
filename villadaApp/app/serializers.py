from rest_framework import serializers

from .models import Comunicado, Directivo


class ComunicadoSer(serializers.HyperlinkedModelSerializer):
    directivo = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Comunicado
        fields = ('titulo', 'fecha', 'directivo', 'mensaje', 'curso')