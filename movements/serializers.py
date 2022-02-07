from rest_framework import serializers
from .models import Movement
from users.models import User


class RegisterMovementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movement

    def validate(self, data):
        user = User.objects.get(pk=data['sender_id'].id)

        if data['receiver_id'] == data['sender_id']:
            raise serializers.ValidationError('receiver and sender could not be the same')
        if data['amount'] < 0:
            raise serializers.ValidationError('amount could not be under 0')
        if user.balance <= 0 or user.balance < data['amount']:
            raise serializers.ValidationError('You don\'t have enough money')
        return data


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movement
