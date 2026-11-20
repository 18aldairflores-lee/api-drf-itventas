from django.db import models

class Articulo(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    condicion = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre