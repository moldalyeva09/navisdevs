from django.urls import path
from directions.views import *

urlpatterns = [
    path('direct/',DirectionsViewSet.as_view()),
    path('information/',InformationViewSet.as_view()),
]

