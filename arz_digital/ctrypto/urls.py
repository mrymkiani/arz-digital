from django.urls import path
from .views import get

urlpatterns = [
    path('crypto/<str: srccurrency>' , get)
]