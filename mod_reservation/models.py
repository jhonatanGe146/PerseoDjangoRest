from django.db import models
from mod_user.models import Persona
from mod_guest.models import Huesped
from mod_room.models import habitacion

# Create your models here.
class Reserva(models.Model):
    fecha_entrada = models.DateTimeField(null=False)
    fecha_salida = models.DateTimeField(null=False)
    precio_calculado= models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cantidad_adultos = models.IntegerField()
    cantidad_ninos = models.IntegerField()
    numero_documento = models.ForeignKey(Persona, on_delete=models.CASCADE)
  
    def __str__(self):
      return self.numero_documento.nombre  
    
class huespedxreserva(models.Model):
    nro_documento = models.ForeignKey(
        Huesped, 
        on_delete=models.CASCADE,
        )
    id_reserva = models.ForeignKey(
        Reserva, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (f'{self.nro_documento} --> {self.id_reserva}')
  
class habitacionxreserva(models.Model):
    num_habitacion = models.ForeignKey(
        habitacion, 
        on_delete=models.CASCADE,
        )
    id_reserva = models.ForeignKey(
        Reserva, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return (f'{self.num_habitacion} --> {self.id_reserva}')