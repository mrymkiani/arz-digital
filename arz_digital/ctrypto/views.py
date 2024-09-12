from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from .models import Crypto ,  Alert
from .serializer import CryptoSerializer


# Create your views here.
