from rest_framework import serializers
from .models import TDR

class TDRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDR
        fields = '__all__'