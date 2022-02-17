from rest_framework import serializers
from .models import Vault
from datetime import date


class VaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vault
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['date'] <= date.today():
            raise serializers.ValidationError('Date is incorrect')
