from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterMovementSerializer
from rest_framework import status
from users.models import User


class RegisterMovement(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = RegisterMovementSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(pk=request.auth.get('user_id'))
            serializer.save()
            user.movements.add(serializer.validated_data.get('movement_id'))
            return Response('Transaction successful', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
