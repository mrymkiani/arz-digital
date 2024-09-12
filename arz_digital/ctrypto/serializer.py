from .models import Crypto , Alert
from rest_framework.serializers import ModelSerializer

class CryptoSerializer(ModelSerializer):
    class Meta:
        model = Crypto
        fields = '__all__'

class AlertSerializer(ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'