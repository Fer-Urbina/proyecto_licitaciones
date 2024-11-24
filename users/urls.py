from django.urls import path
from .views import listar_proveedores, buscar_proveedor_por_nombre

urlpatterns = [
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/buscar/', buscar_proveedor_por_nombre, name='buscar_proveedor_por_nombre'),
]