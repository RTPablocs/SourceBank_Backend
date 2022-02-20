from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import UntypedToken
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode
from django.conf import settings
from users.models import User
from itertools import chain
from urllib.parse import parse_qs
from .serializers import LoggedUserSerializer


@database_sync_to_async
def get_user(user_id):
    try:
        user = User.objects.get(pk=user_id)
        received_movements = user.receiver.all()
        sent_movements = user.sender.all()
        user.movements = list(chain(received_movements, sent_movements))
        user.notifications = user.user_nots.all()
        user.vaults = user.user_vaults.all()
        return LoggedUserSerializer(user).data
    except User.DoesNotExist:
        return None


class AuthorizationMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        token_arg = parse_qs(scope['query_string'].decode('utf-8'))['token'][0]
        try:
            UntypedToken(token_arg)
        except (InvalidToken, TokenError) as error:
            return AnonymousUser()

        else:
            user_data = decode(token_arg, settings.SECRET_KEY, algorithms=['HS256'])
            scope['token'] = token_arg
            scope['user'] = await get_user(user_data['user_id'])
            return await self.app(scope, receive, send)
