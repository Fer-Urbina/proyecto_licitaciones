from django.db import models
from licitaciones.models import Licitacion

class TDR(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE, related_name="tdrs")
    especificacion = models.TextField()
    prioridad = models.CharField(max_length=50)

    def __str__(self):
        return f"TDR for {self.licitacion.titulo}"