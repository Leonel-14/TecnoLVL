from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    
    #esto hace que el username ahora sea nombre de usuario
    
    def __str__(self):
        return f"{self.nombre,self.apellido,self.email}"
    