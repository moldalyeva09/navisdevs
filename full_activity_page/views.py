from rest_framework import viewsets
from full_activity_page.models import ActivityTitle
from full_activity_page.serializer import ActivityTitleSerializer


class ActivityTitleViewSet(viewsets.ModelViewSet):
    queryset = ActivityTitle.objects.all()
    serializer_class = ActivityTitleSerializer
