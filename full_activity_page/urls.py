from django.urls import path
from full_activity_page.views import *

urlpatterns = [
    path('full_page_act/',ActivityTitleViewSet.as_view),
]