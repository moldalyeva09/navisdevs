from django.contrib import admin

from vacancy.models import Application, Job_title

admin.site.register(Job_title)
admin.site.register(Application)

