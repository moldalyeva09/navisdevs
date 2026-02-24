from django.urls import path
from vacancy_main_page.views import JobsViewSet


urlpatterns = [
    path('jobs/',JobsViewSet.as_view)
]