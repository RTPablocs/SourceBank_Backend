from django.db import models
from users.models import User


# Create your models here.
class Vault(models.Model):
    vault_id = models.AutoField(primary_key=True)
    vault_name = models.CharField(null=False, max_length=100)
    vault_desc = models.CharField(null=True, max_length=240)
    vault_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vault_date = models.DateField(null=True)
    vault_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
