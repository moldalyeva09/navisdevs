from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets

from contact.models import Contact
from contact.serializer import ContactSerializer
import requests

TOKEN = "8590383433:AAH7KF8RTZP26pRPp3WwKVGNm4jMZ8yPnyo"
CHAT_ID = "-1003702648842"   # группа ID

class SendTelegramMessageView(View):
    def post(self, request):
        name = request.POST.get("name")
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": f"Жаңы колдонуучу: {name}"
        }
        requests.post(url, data=data)
        return HttpResponse("Жиберилди!")


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

