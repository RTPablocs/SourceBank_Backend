from rest_framework import permissions


class IsHimself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user_id = request.auth.payload.get('user_id')
        request_id = request.resolver_match.kwargs.get('pk')
        if user_id == int(request_id):
            return True
        else:
            return False
