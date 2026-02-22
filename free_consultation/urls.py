from django.urls import path

from free_consultation.views import *

urlpatterns = [
    path("consultation/", ConsultationViewSet.as_view),
    path("completed/", CompletedViewSet.as_view),
]

