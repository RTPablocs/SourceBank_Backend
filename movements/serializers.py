from rest_framework import serializers
from .models import Movement


class RegisterMovementSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Movement

    def validate(self, data):
        if data['receiver_id'] == data['sender_id']:
            raise serializers.ValidationError('receiver and sender could not be the same')
        if data['amount'] < 0:
            raise serializers.ValidationError('amount could not be under 0')
        return data