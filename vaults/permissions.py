from rest_framework.permissions import BasePermission
from .models import Vault
from .serializers import VaultSerializer


class IsMyOwnVault(BasePermission):
    def has_permission(self, request, view):
        try:
            db_vault = VaultSerializer(Vault.objects.get(id=request.data['vault']))
        except KeyError:
            db_vault = VaultSerializer(Vault.objects.get(id=request.parser_context['kwargs']['vault_id']))

        if db_vault['owner'].value == request.auth.payload['user_id']:
            return True
        return False


class VaultHasNoBalance(BasePermission):
    message = 'Sorry, this vault isn\'t empty'

    def has_permission(self, request, view):
        try:
            db_vault = VaultSerializer(Vault.objects.get(id=request.data['vault']))
        except KeyError:
            db_vault = VaultSerializer(Vault.objects.get(id=request.parser_context['kwargs']['vault_id'])).data

        amount = float(db_vault['amount'])
        if amount == 0:
            return True
        return False
