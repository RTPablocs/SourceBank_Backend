from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoggedUserSerializer
from rest_framework import permissions
from .permissions import IsNotAuthenticated
from .models import User
from rest_framework import status
from itertools import chain


class RegisterAPIView(APIView):
    permission_classes = [IsNotAuthenticated]

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveMyOwnData(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user_id = request.auth['user_id']
        user = User.objects.get(pk=user_id)
        received_movements = user.receiver.all()
        sent_movements = user.sender.all()
        user.movements = list(chain(received_movements, sent_movements))
        user.notifications = user.user_nots.all()
        user.vaults = user.user_vaults.all()
        serializer = LoggedUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
