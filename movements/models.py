from django.db import models
from users.models import User
from vaults.models import Vault


class AbstractMovement(models.Model):
    movement_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=2, null=False)


class Movement(AbstractMovement):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(null=False, max_length=140)


class VaultMovement(AbstractMovement):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE, related_name='vault')
