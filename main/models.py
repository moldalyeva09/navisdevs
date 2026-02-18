from django.db import models


class Main(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Image(models.Model):
    img = models.ImageField(null=True, blank=True)

class Instr(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True)

class Url(models.Model):
    text = models.CharField(max_length=150)
    img = models.ImageField(upload_to='url/')
    url = models.URLField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.text


class Comment(models.Model):
    name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='comment/')
    text = models.TextField()

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    message = models.TextField()
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField()
    working_hours = models.CharField()

    def __str__(self):
        return self.name


# Create your models here.
