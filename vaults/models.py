from django.db import models
from users.models import User


# Create your models here.
class Vault(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)
    desc = models.CharField(null=True, max_length=240)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    target = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_vaults')

