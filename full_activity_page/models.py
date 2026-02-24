from django.db import models



class ActivityTitle(models.Model):
    img = models.ImageField(upload_to= 'act.img/', blank=True, null=True)
    title = models.CharField(max_length=150)
    benefits = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.title