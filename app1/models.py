from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    is_verify = models.BooleanField(default=False)
    height = models.CharField(max_length=200, default=0)
    weight = models.CharField(max_length=300, default=0)
    auth_token = models.CharField(max_length=100)


    class Meta:
        db_table = 'custom_user'





