from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from full_activity_page.models import ActivityTitle
from full_activity_page.serializer import ActivityTitleSerializer


class ActivityTitleViewSet(viewsets.ModelViewSet):
    queryset = ActivityTitle.objects.all()
    serializer_class = ActivityTitleSerializer


class TestView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
