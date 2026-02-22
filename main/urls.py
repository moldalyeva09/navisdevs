from django.urls import path

from .serializers import UrlSerializer
from .views import *



urlpatterns = [
    path('api/service/', ServiceListAPIView.as_view(),name='service-list'),
    path('main/', MainList.as_view()),
    path('main/create/', MainCreate.as_view()),
    path('image/',ImageCreate.as_view()),
    path('instr/', InstrCreate.as_view()),
    path('url/',UrlListCreate.as_view()),
    path('comment/',CommentListCreate.as_view()),
    path('application/',ApplicationCreate.as_view())
]