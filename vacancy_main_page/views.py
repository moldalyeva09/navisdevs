from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from vacancy_main_page.models import Jobs
from vacancy_main_page.serializer import JobsSerializer


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


class TestView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]