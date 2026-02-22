from django.shortcuts import render
from rest_framework import viewsets

from directions.models import Directions,Information
from directions.serializer import DirectionsSerializer,InformationSerializer


class DirectionsViewSet(viewsets.ModelViewSet):
    queryset = Directions.objects.all()
    serializer_class = DirectionsSerializer

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer