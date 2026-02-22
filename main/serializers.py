from rest_framework import serializers
from .models import Main, Comment, Application, Image, Instr, ServiceItem
from .models import Url


class MainSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)
    class Meta:
        model = Main
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class InstrSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)
    class Meta:
        model = Instr
        fields = '__all__'


class UrlSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)
    url = serializers.URLField(required=False)
    class Meta:
        model = Url
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)

    class Meta:
        model = Comment
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)
    class Meta:
        model = Application
        fields = '__all__'

    class ServiceItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = ServiceItem
            fields = ['id', 'name', 'description']
    # def validate_phone_number(self,number):






