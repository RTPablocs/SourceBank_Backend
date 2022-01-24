from rest_framework import permissions
import jwt
from SourceBank.settings import SECRET_KEY


class IsHimself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.META['Authorization'].replace('Bearer ', '')
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        request_id = request.query_params('id')
        if payload.get('id') == request_id:
            return True
        else:
            return False

