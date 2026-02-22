from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import requests


class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    asks = models.TextField()
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100)
    worktime = models.CharField(max_length=100)

    def __str__(self):
        return self.surname


@receiver(post_save, sender=Contact)
def notify_group(sender, instance, created, **kwargs):
    if created:
        requests.post(
            f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage",
            data={
                "chat_id": settings.TELEGRAM_CHAT_ID,
                "text": f"Жаңы объект түзүлдү: {instance.name}"
            }
        )

