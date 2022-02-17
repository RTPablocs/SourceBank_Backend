from rest_framework.views import APIView
from .models import Vault
from .permissions import IsMyOwnVault, VaultHasNoBalance
from rest_framework.permissions import IsAuthenticated
from .serializers import VaultSerializer
from rest_framework import status
from rest_framework.response import Response


class UpdateVault(APIView):
    permission_classes = [IsAuthenticated, IsMyOwnVault]

    def patch(self, request):
        vault_id = request.data['id']
        request.data.pop('id')
        Vault.objects.filter(id=vault_id).update(**request.data)
        return Response({'message': 'vault has been updated'}, status=status.HTTP_200_OK)


class CreateVault(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['owner'] = request.auth['user_id']
        serializer = VaultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Vault Created'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DropVault(APIView):
    permission_classes = [IsAuthenticated, IsMyOwnVault, VaultHasNoBalance]

    def delete(self, request):
        vault_id = request.data['id']
        Vault.objects.filter(id=vault_id).delete()
        return Response({'message': 'vault has been deleted'}, status=status.HTTP_200_OK)
