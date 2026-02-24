from django.db import models
# страница одной вакансии


class Jobs(models.Model):
    job_time = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

