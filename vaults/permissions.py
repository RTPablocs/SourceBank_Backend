from rest_framework.permissions import BasePermission
from .models import Vault
from .serializers import VaultSerializer


class IsMyOwnVault(BasePermission):
    def has_permission(self, request, view):
        db_vault = VaultSerializer(Vault.objects.get(id=request.data['id']))
        if db_vault['owner'] == request.auth['user_id']:
            return True
        return False


class VaultHasNoBalance(BasePermission):
    message = 'Sorry, this vault isn\'t empty'

    def has_permission(self, request, view):
        db_vault = VaultSerializer(Vault.objects.get(id=request.data['id']))
        if db_vault['balance'] == 0:
            return True
        return False
