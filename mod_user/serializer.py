from rest_framework import serializers
from .models import Persona, TipoDocumento, TipoPersona

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPersona
        fields = "__all__"

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = "__all__"