from rest_framework import serializers
from .models import ActivityTitle


class ActivityTitleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        name = ActivityTitle
        fields = '__all__'