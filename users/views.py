from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Proveedor
from .serializers import ProveedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    serializer = ProveedorSerializer(proveedores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buscar_proveedor_por_nombre(request):
    nombre = request.query_params.get('nombre', None)
    if nombre:
        proveedores = Proveedor.objects.filter(nombre__icontains=nombre)
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Debe proporcionar un nombre'}, status=status.HTTP_400_BAD_REQUEST)