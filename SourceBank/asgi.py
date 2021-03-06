"""
ASGI config for SourceBank project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from users.middlewares import AuthorizationMiddleware
from django.core.asgi import get_asgi_application
import users.routers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SourceBank.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthorizationMiddleware(
        URLRouter(
            users.routers.websocket_urlpatterns
        )
    )})
