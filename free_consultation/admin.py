from django.contrib import admin

from free_consultation.models import Consultation, Completed
from .models import *
admin.site.register(Consultation)
admin.site.register(Completed)
# Register your models here.
