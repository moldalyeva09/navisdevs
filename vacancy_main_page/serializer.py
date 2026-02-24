from rest_framework import serializers
from .models import Jobs


class JobsSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()

    class Meta:
        name = Jobs
        fields = '__all__'