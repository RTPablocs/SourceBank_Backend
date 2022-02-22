from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from vaults.permissions import IsMyOwnVault
from .serializers import RegisterMovementSerializer, RegisterVaultMovementSerializer
from rest_framework import status
from users.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class RegisterMovement(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['sender_id'] = request.auth.get('user_id')
        user_name = request.data.pop('username')
        try:
            request.data['receiver_id'] = User.objects.get(username=user_name).id
        except User.DoesNotExist:
            return Response({"error": "user does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RegisterMovementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Transaction successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterVaultMovement(APIView):
    permission_classes = [IsAuthenticated, IsMyOwnVault]

    def post(self, request):
        data = request.data
        data['user'] = request.auth['user_id']
        serializer = RegisterVaultMovementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Transaction successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
