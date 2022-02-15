from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'user/me/', consumer.UserConsumer.as_asgi())
]
