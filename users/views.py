from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoggedUserSerializer
from rest_framework import permissions
from .models import User
from movements.models import Movement
from rest_framework import status
from django.db.models import Q


class RegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveMyOwnData(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # TODO Fix Single Object Serialization when query returns only one movement
    def get(self, request, format=None):
        user_id = request.auth.get('user_id')
        user = User.objects.get(pk=user_id)
        user.movements = Movement.objects.get(Q(receiver_id_id=user_id) | Q(sender_id_id=user_id))
        serializer = LoggedUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
