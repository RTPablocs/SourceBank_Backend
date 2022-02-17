from rest_framework import serializers
from .models import Vault
from datetime import date


class VaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vault
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['amount'] < 0:
            raise serializers.ValidationError('Amount could not be under 0')
        return super(VaultSerializer, self).create(validated_data)
