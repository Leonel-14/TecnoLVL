from django.db import models

class Barrio(models.Model):
    nombre = models.CharField(max_length=50)
    id_ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.id_ciudad}"  # Muestra el nombre de la ciudad relacionada


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    id_provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.id_provincia}"  # Muestra el nombre de la provincia relacionada


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    id_pais = models.ForeignKey('Pais', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.id_pais}"  # Muestra el nombre del país relacionado


class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre
