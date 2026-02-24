from rest_framework import viewsets
from activity.models import Activity
from activity.serializer import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
