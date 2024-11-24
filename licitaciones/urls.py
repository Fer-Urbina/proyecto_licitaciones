from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LicitacionViewSet

router = DefaultRouter()
router.register(r'licitaciones', LicitacionViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Todas las rutas generadas automáticamente
]
