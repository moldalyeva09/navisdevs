from .views import *
from django.urls import path
from .views import SendTelegramMessageView


urlpatterns = [
    path("send/", SendTelegramMessageView.as_view()),
]