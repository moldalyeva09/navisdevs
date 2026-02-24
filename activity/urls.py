from activity.views import ActivityViewSet
from django.urls import path



urlpatterns = [
    path ('activity/', ActivityViewSet.as_view),
]