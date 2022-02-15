from django.db import models
from users.models import User


# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification_title = models.CharField(max_length=25)
    notification_message = models.CharField(max_length=240)
    notification_status = models.IntegerField(default=0)
    notification_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_nots')
