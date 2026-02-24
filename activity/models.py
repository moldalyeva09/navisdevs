from django.db import models



class Activity(models.Model):
    img = models.ImageField(upload_to='activity', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=50)
    time = models.TimeField()
    address = models.CharField(max_length=150)


    def __str__(self):
        return self.title
# Create your models here.
