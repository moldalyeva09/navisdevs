from rest_framework import serializers
from .models import Job_title , Application


class TitleSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()

    class Meta:
        name = Job_title
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()

    class Meta:
        name = Application
        fields = '__all__'
