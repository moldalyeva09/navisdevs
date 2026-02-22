from rest_framework import serializers
from .models import ServiceItem



class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        fields = ['id', 'name', 'description']
