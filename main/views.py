from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from main.models import Main, Url, Comment, Application, Image, Instr
from main.serializers import MainSerializer
from main.models import ServiceItem


class MainList(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

class MainCreate(generics.CreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

class ImageCreate(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = MainSerializer

class InstrCreate(generics.CreateAPIView):
    queryset = Instr.objects.all()
    serializer_class = MainSerializer


class UrlListCreate(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = MainSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = MainSerializer

class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class=MainSerializer

class ServiceListAPIView(generics.ListAPIView):
    queryset = ServiceItem.objects.prefetch_related('items').all()
    serializer_class = MainSerializer

class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,reguest):
        return Response({'user':reguest.user.username})



# Create your views here.
