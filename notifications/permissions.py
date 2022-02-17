from rest_framework.permissions import BasePermission
from .models import Notification
from .serializers import CheckNotificationSerializer


class IsMyNotification(BasePermission):
    def has_permission(self, request, view):
        req_notification = request.data
        db_notification = CheckNotificationSerializer(Notification.objects.get(id=req_notification['id']))
        if db_notification.data['receiver'] == request.auth['user_id']:
            return True
        else:
            return False
