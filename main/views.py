from django.shortcuts import render
from rest_framework import generics

from main.models import Main, Url, Comment, Application, Image, Instr
from main.serializers import MainSerializer, InstrSerializer


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
    serializer_class = InstrSerializer


class UrlListCreate(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = MainSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = MainSerializer

class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class=MainSerializer




# Create your views here.
