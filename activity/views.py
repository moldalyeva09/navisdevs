from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from activity.models import Activity
from activity.serializer import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TestView(APIView):
    permission_classes = [AllowAny]