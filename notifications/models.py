from django.db import models
from users.models import User


# Create your models here.
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    message = models.CharField(max_length=240)
    status = models.IntegerField(default=0)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_nots')
    date = models.DateTimeField(auto_now_add=True)
