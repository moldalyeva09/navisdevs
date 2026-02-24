from django.urls import path

from vacancy.views import *

urlpatterns = [
    path('vacancy/',TitleViewSet.as_view),
    path("application/", ApplicationViewSet.as_view),
]