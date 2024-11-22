from django.db import models

# Create your models here.

class Licitacion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo