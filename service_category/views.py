from django.shortcuts import render
from rest_framework import generics
from .models import ServiceItem
from .serializers import  ServiceItemSerializer

class ServiceListAPIView(generics.ListAPIView):
    queryset = ServiceItem.objects.prefetch_related('items').all()
    serializer_class = ServiceItemSerializer

# Create your views here.
