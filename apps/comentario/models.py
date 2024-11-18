from django.db import models
from apps.usuario.models import Usuario
from apps.producto.models import Producto
# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario,self.producto,self.descripcion,self.fecha}"