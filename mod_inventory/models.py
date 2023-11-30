from django.db import models

# Create your models here.
class categoria_inventario(models.Model):
    nombre_categoria = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=500)
  
    def __str__(self):
        return self.nombre_categoria


class estado_producto(models.Model):
    nombre_estado = models.CharField(max_length=60)
  
    def __str__(self):
        return self.nombre_estado


class inventario(models.Model):
    nombre_producto = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=500)

    id_estado= models.ForeignKey(
            estado_producto,
            on_delete=models.CASCADE,
      
        )
    id_categoria= models.ForeignKey(
        categoria_inventario,
        on_delete=models.CASCADE,
 
    )
   
    def __str__(self):
        return (f"{self.nombre_producto} --> {self.id_categoria}")
