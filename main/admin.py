from django.contrib import admin
from rest_framework import generics

from .models import Main, Comment, Application, Image, Instr, ServiceItem
from .models import Url

admin.site.register(ServiceItem)
admin.site.register(Instr)
admin.site.register(Image)
admin.site.register(Url)
admin.site.register(Comment)
admin.site.register(Application)
admin.site.register(Main)


