from rest_framework import serializers
from .models import Consultation, Completed


class ConsultationSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()

    class Meta:
        name = Consultation
        fields = '__all__'

class CompletedSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        name = Completed
        fields = '__all__'
