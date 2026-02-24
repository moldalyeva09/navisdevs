from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()

    class Meta:
        name = Activity
        fields = '__all__'