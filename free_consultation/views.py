from django.shortcuts import render
from rest_framework import viewsets

from free_consultation.models import Consultation , Completed
from free_consultation.serializer import CompletedSerializer,ConsultationSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class CompletedViewSet(viewsets.ModelViewSet):
    queryset = Completed.objects.all()
    serializer_class = CompletedSerializer

