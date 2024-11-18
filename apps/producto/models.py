from django.db import models

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.PositiveIntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=255)
    marca = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre,self.precio,self.tipo,self.imagen,self.marca,self.descripcion}"
    
    
    