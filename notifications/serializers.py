from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['receiver']
        model = Notification


class CheckNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Notification
