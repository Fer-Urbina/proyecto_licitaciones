from rest_framework import serializers
from .models import Licitacion

class LicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacion
        fields = '__all__'