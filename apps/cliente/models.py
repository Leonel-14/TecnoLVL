from django.db import models
from apps.ubicacion.models import Barrio
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    edad = models.IntegerField()
    correo = models.EmailField()
    contraseña = models.CharField(max_length=40)
    telefono = models.IntegerField()
    id_barrio = models.ForeignKey(Barrio,on_delete=models.CASCADE)
    calle = models.CharField(max_length=40)
    altura = models.IntegerField()
    piso = models.IntegerField()
    departamento = models.CharField(max_length=3)
    codigo_postal = models.IntegerField()

    
    
