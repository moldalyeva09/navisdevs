from rest_framework import viewsets
from vacancy_main_page.models import Jobs
from vacancy_main_page.serializer import JobsSerializer


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

# Create your views here.
