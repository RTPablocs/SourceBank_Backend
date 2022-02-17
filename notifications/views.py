from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .permissions import IsMyNotification
from rest_framework import status


class UpdateNotification(APIView):
    permission_classes = [IsAuthenticated, IsMyNotification]

    def patch(self, request):
        Notification.objects.filter(id=request.data['id']).update(status=request.data['status'])
        return Response({'message': 'notification updated'}, status=status.HTTP_200_OK)
