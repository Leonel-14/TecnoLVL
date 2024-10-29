from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30) 

    def __str__(self):
        return f"{self.nombre}"

class EstadoProducto(models.Model):
    nombre = models.CharField(max_length=15) #Disponible #No Disponible

    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    id_estado_producto = models.ForeignKey(EstadoProducto,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=100)

    






    