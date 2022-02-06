from django.db import models
from users.models import User


class Movement(models.Model):
    movement_id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True),
    status = models.IntegerField(default=1, null=False)

# Create your models here.
