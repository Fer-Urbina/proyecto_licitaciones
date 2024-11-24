from django.urls import path
from .views import listar_tdrs_por_licitacion, actualizar_tdr

urlpatterns = [
    path('licitaciones/<int:licitacion_id>/tdrs/', listar_tdrs_por_licitacion, name='listar_tdrs_por_licitacion'),
    path('tdrs/<int:tdr_id>/actualizar/', actualizar_tdr, name='actualizar_tdr'),
]