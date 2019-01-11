from django.db import models
from auths.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

class Box(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    price = models.FloatField(default=0)

class TransAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
