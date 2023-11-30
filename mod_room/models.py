from django.db import models
from mod_inventory.models import inventario

# Create your models here.
class estado_habitacion(models.Model):
    tipo_estado = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200)
 
    def __str__(self):
        return self.tipo_estado

 

class tipo_habitacion(models.Model):
    tipo_habitacion = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=500)
    precioxnoche = models.FloatField()
    cantidad_adultos = models.IntegerField()
    cantidad_ninos = models.IntegerField()
    foto = models.ImageField(upload_to='fotos_tipoHab')

    def __str__(self):
        return self.tipo_habitacion


class habitacion(models.Model):
    num_habitacion = models.CharField(max_length=4, primary_key=True)
    id_estadoHab = models.ForeignKey(
        estado_habitacion,
        on_delete=models.CASCADE,
    )
    id_tipoHab = models.ForeignKey(
        tipo_habitacion,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.num_habitacion

class inventarioxhabitacion (models.Model):
    num_habitacion = models.ForeignKey(
        habitacion, 
        on_delete=models.CASCADE,
        )
    id_inventario = models.ForeignKey(
        inventario, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (f'{self.num_habitacion} --> {self.id_inventario}')