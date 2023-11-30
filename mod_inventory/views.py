from .models import estado_producto, categoria_inventario
from rest_framework import viewsets
from .serializer import EstadoProductoSerializer, CategoriaInventarioSerializer

class EstadoProductoViewSet(viewsets.ModelViewSet):
    queryset = estado_producto.objects.all()
    serializer_class = EstadoProductoSerializer


class CategoriaInventarioViewSet(viewsets.ModelViewSet):
    queryset = categoria_inventario.objects.all()
    serializer_class = CategoriaInventarioSerializer



