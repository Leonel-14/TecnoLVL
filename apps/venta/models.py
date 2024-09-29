from django.db import models
from apps.producto.models import Producto
# Create your models here.
class EstadoVenta(models.Model):
    nombre = models.CharField(max_length=20)
    #En preparacion
    #En camino
    #Entregado

    def __str__(self) -> str:
        return f"{self.nombre}"

class Venta(models.Model):
    id_estado_venta = models.ForeignKey(EstadoVenta,on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total_venta = models.FloatField()

class DetalleVenta(models.Model):
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    sub_total = models.FloatField()
