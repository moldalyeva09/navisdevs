from django.db import models
from rest_framework.fields import ImageField


class Consultation(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    ask = models.TextField()

    def __str__(self):
        return self.name

class Completed(models.Model):
    img = models.ImageField(upload_to='img/', blank=True)
    message = models.CharField(max_length=200)
    message2 = models.CharField(max_length=300)

    def __str__(self):
        return self.message