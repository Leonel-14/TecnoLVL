from django.db import models
from apps.cliente.models import Cliente
from apps.venta.models import Venta
# Create your models here.
class Orden(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion_establecida = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
