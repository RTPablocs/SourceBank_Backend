from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)

    class Meta:
        model = User
        exclude = ['last_login', 'is_staff', 'date_joined', 'is_superuser', 'groups', 'user_permissions']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegisterSerializer, self).create(validated_data)


class LoggedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'is_staff', 'date_joined', 'is_superuser', 'groups', 'user_permissions', 'password',
                   'is_active']
