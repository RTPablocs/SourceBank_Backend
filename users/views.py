from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import RegisterSerializer, LoggedUserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework import status


class RegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetOrUpdateOwnData(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = LoggedUserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
