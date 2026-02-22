from django.urls import path
from .views import ServiceListAPIView

urlpatterns = [
    path('api/service/', ServiceListAPIView.as_view(),
    name='service-list')
]
