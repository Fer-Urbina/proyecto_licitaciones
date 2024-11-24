from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Licitacion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser después de la fecha de fin.")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)