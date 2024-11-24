from django.http import HttpResponse
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Licitacion
from .serializers import LicitacionSerializer
from .utils import notify_proveedor
from tdrs.models import TDR
from tdrs.serializers import TDRSerializer

# Vista para la página de inicio
def home(request):
    return HttpResponse("Bienvenido a la API de Licitaciones")

# ViewSet para manejar las licitaciones
class LicitacionViewSet(viewsets.ModelViewSet):
    queryset = Licitacion.objects.all()
    serializer_class = LicitacionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descripcion']
    ordering_fields = ['fecha_inicio', 'fecha_fin']

    # Acción personalizada para actualizar el estado de una licitación
    @action(detail=True, methods=["post"])
    def actualizar_estado(self, request, pk=None):
        """
        Actualiza el estado de una licitación y envía una notificación al proveedor.
        """
        licitacion = self.get_object()
        nuevo_estado = request.data.get("estado")
        
        if nuevo_estado:
            licitacion.estado = nuevo_estado
            licitacion.save()
            
            # Enviar notificación al proveedor
            notify_proveedor(licitacion)
            
            return Response({
                "mensaje": f"Estado actualizado a '{nuevo_estado}' y notificación enviada."
            })
        return Response({"error": "Debe proporcionar un estado."}, status=400)

    # Acción personalizada para obtener los TDRs relacionados a una licitación
    @action(detail=True, methods=["get"])
    def tdrs(self, request, pk=None):
        """
        Retorna los TDRs asociados a una licitación específica.
        """
        licitacion = self.get_object()
        tdrs = TDR.objects.filter(id_licitacion=licitacion.id)
        serializer = TDRSerializer(tdrs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)