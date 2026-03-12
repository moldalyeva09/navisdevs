from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from vacancy.models import Job_title, Application
from vacancy.serializer import TitleSerializer, ApplicationSerializer
from rest_framework.permissions import IsAuthenticated

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Job_title.objects.all()
    serializer_class = TitleSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class TestView(APIView):
    permission_classes = [IsAuthenticated]
