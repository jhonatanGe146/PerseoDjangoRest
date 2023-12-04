from .models import TipoDocumento, TipoPersona, Persona
from rest_framework import viewsets
from .serializer import UsuarioSerializer, TipoDocumentoSerializer, TipoUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = UsuarioSerializer


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoPersona.objects.all()
    serializer_class = TipoUsuarioSerializer


