from django.db import models
from django.contrib.auth.models import User
class Crypto(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=20 , decimal_places=2)
    price_chane_24 = models.DecimalField(max_digits=20 ,  decimal_places=2)
    def __str__(self) -> str:
        return self.user.name

class Crypto(models.Model):
    pass
    

# Create your models here.
