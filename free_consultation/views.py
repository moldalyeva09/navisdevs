from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from free_consultation.models import Consultation , Completed
from free_consultation.serializer import CompletedSerializer,ConsultationSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class CompletedViewSet(viewsets.ModelViewSet):
    queryset = Completed.objects.all()
    serializer_class = CompletedSerializer

class TestView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
