from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import CheckNotificationSerializer
from rest_framework import status


class UpdateNotification(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        notification = CheckNotificationSerializer(Notification.objects.get(id=request.data['id']))
        if notification.data['receiver'] == request.auth['user_id']:
            Notification.objects.filter(id=request.data['id']).update(status=request.data['status'])
            return Response({'message': 'notification updated'}, status=status.HTTP_200_OK)
        return Response({'error': 'this notification does not belong to you and cannot be updated'})
