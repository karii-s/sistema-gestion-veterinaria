from django.db import models


class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre