from django.shortcuts import render
from rest_framework import viewsets

from vacancy.models import Job_title, Application
from vacancy.serializer import TitleSerializer, ApplicationSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Job_title.objects.all()
    serializer_class = TitleSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

# Create your views here.
