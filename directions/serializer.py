from rest_framework import serializers
from .models import Directions,Information


class DirectionsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        name = Directions
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        name = Information
        fields = '__all__'
