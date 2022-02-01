from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoggedUserSerializer
from rest_framework import permissions
from .models import User
from rest_framework import status


class RegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveMyOwnData(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        user = User.objects.get(pk=request.auth.get('user_id'))
        serializer = LoggedUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
