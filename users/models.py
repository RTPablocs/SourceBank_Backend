from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'email', 'country', 'city', 'phone']

    photo = models.ImageField(null=True, upload_to='users')
    city = models.CharField(null=False, max_length=120)
    country = models.CharField(null=False, max_length=150)
    phone = models.CharField(null=False, max_length=190)
