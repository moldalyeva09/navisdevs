from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from directions.models import Directions,Information
from directions.serializer import DirectionsSerializer,InformationSerializer


class DirectionsViewSet(viewsets.ModelViewSet):
    queryset = Directions.objects.all()
    serializer_class = DirectionsSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

class TestView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]