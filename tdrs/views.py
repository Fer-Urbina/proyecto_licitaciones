from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import TDR
from .serializers import TDRSerializer
from licitaciones.models import Licitacion

class TDRViewSet(viewsets.ModelViewSet):
    queryset = TDR.objects.all()
    serializer_class = TDRSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_tdrs_por_licitacion(request, licitacion_id):
    tdrs = TDR.objects.filter(id_licitacion=licitacion_id)
    serializer = TDRSerializer(tdrs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def actualizar_tdr(request, tdr_id):
    tdr = get_object_or_404(TDR, pk=tdr_id)
    serializer = TDRSerializer(tdr, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)