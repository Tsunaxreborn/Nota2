from django.db import models

# Create your models here.
from django.utils import timezone
class Automovil(models.Model):
    titulo = models.CharField(max_length=200)
    Marca = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Año_automovil = models.DateTimeField(
        default=timezone.now)
    Color = models.CharField(max_length=200)
    Numero_puertas = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Fecha_publicacion = models.DateTimeField(
        blank=True, null=True)
    Precio = models.CharField(max_length=200)
    def publish(self):
        self.Fecha_publicacion = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo
