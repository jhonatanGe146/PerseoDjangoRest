from .models import habitacion,estado_habitacion,tipo_habitacion,inventario, inventarioxhabitacion
from rest_framework import viewsets
from .serializer import HabitacionSerializer, EstadoHabitacionSerializer, TipoHabitacionSerializer, InventarioSerializer, InventarioXHabitacionSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = habitacion.objects.all()
    serializer_class = HabitacionSerializer


class TipoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = tipo_habitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

class EstadoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = estado_habitacion.objects.all()
    serializer_class = EstadoHabitacionSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = inventario.objects.all()
    serializer_class = InventarioSerializer


class InventarioXHabitacionViewSet(viewsets.ModelViewSet):
    queryset = inventarioxhabitacion.objects.all()
    serializer_class = InventarioXHabitacionSerializer

