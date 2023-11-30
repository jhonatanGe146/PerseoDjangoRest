from django.db import models
from mod_user.models import Persona

class DetallesFactura(models.Model):
    fecha_emision = models.DateTimeField(null=False)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return str(self.fecha_emision)

class MetodoPago(models.Model):
    metodo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.metodo

class Factura(models.Model):
    id_metodoPago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    id_detalleFactura = models.ForeignKey(DetallesFactura, on_delete=models.CASCADE)
    numero_documento = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_metodoPago)