from django.test import TestCase
from .models import Licitacion

class LicitacionTestCase(TestCase):
    def setUp(self):
        Licitacion.objects.create(
            titulo="Licitación 1",
            descripcion="Descripción de prueba",
            fecha_inicio="2024-01-01",
            fecha_fin="2024-12-31",
            estado="Abierta",
            presupuesto=50000.00,
        )

    def test_licitacion_presupuesto(self):
        licitacion = Licitacion.objects.get(titulo="Licitación 1")
        self.assertEqual(licitacion.presupuesto, 50000.00)