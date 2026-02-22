from django.db import models

from free_consultation.models import Consultation


class Directions(models.Model):
    image = models.ImageField(upload_to='img/', blank=True)
    direc = models.CharField(max_length=200)

    def __str__(self):
        return self.direc

class Information(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='img/', blank=True,null=True)
    services = models.ManyToManyField(Consultation)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.title


