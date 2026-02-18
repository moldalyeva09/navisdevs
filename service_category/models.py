from django.db import models


class ServiceItem(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=250, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


