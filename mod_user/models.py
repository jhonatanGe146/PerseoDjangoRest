from django.db import models

# Create your models here.
class TipoPersona(models.Model):
    tipo_persona = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo_persona

class TipoDocumento(models.Model):
    tipo_documento = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo_documento

class Persona(models.Model):
    id_tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    id_tipoPersona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre