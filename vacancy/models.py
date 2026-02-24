from django.db import models
# страница одной вакансии
class Job_title(models.Model):
    title = models.CharField(max_length=200)
    benefits = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to='jobs/',blank=True,null=True)
    def __str__(self):
        return self.title

class Application(models.Model):
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    url = models.URLField()

    def __str__(self):
        return self.name


