from django.db import models
from mod_user.models import Persona

# Create your models here.
class reserva(models.Model):
    fecha_entrada = models.DateTimeField(null=False)
    fecha_salida = models.DateTimeField(null=False)
    precio_calculado= models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cantidad_adultos = models.IntegerField()
    cantidad_ninos = models.IntegerField()
    numero_documento = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
  
    def __str__(self):
        return self.numero_documento

