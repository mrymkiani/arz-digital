from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.generics import ListAPIView 
<<<<<<< HEAD
from .models import Crypto , Alert
=======
from .models import Crypto ,  Alert
>>>>>>> 3b14803a26f4d5f9b14f885adc80ac9c930a6de1
from .serializer import CryptoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings
import requests
import json



def get(request ,srccurrency ):
    url = 'https://api.nobitex.ir/v2/market/stats?srcCurrency={}&dstCurrency={}'.format('srccurrency', "rls")
    response = requests.get(url)
    res = {
            "price":json.loads(response.content) . get("Latest") , 
            "price_chane_24":json.loads(response.content).get("dayChange")
        }
    cryptos = Crypto.objects.create(
        crypto =srccurrency , 
        price = res['price'] , 
        price_chane_24 = res['price_chane_24'])
    alerts = Alert.objects.all()
    for alert in alerts:
        if res['price'] >= alert.target_price:
            send_mail(
                'Crypto Alert!',
                f'The price of {alert.crypto.name} has reached {alert.target_price}.',
                settings.DEFAULT_FROM_EMAIL,
                [alert.user.email],
                fail_silently=False,
            )
    return JsonResponse(res)
            

# Create your views here.
