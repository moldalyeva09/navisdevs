"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from activity.views import ActivityViewSet
from contact.views import ContactViewSet
from directions.views import DirectionsViewSet, InformationViewSet

from free_consultation.views import ConsultationViewSet, CompletedViewSet
from full_activity_page.views import ActivityTitleViewSet
from vacancy.views import TitleViewSet, ApplicationViewSet
from vacancy_main_page.views import JobsViewSet

router = routers.SimpleRouter()

router.register('contact', ContactViewSet)
router.register('vacancy', TitleViewSet)
router.register('direct', DirectionsViewSet)
router.register('information', InformationViewSet)
router.register('jobs', JobsViewSet)
router.register('activity', ActivityViewSet)
router.register('consultation', ConsultationViewSet)
router.register('activity_title', ActivityTitleViewSet)
router.register('application', ApplicationViewSet)
router.register('completed',CompletedViewSet)


def home(request):
    return HttpResponse ('Сервер иштеп жатат!')
#
urlpatterns = [
    path('api/', include(router.urls)),
    path("",home),
    path('admin/', admin.site.urls),
    path('',include('main.urls')),

   path('api/token/',TokenObtainPairView.as_view()),
   path('api/token/refresh',TokenRefreshView.as_view()),
 ]
