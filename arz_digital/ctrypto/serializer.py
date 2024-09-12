from .models import Crypto
from rest_framework.serializers import ModelSerializer

class CryptoSerializer(ModelSerializer):
    class Meta:
        model = Crypto
        fields = '__all__'