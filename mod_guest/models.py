from django.db import models

class Huesped(models.Model):
    numero_documento = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre