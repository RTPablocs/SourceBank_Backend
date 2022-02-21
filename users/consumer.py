import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from users.serializers import LoggedUserSerializer
from .models import User
from itertools import chain

from asgiref.sync import async_to_sync


class UserConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def get_user(self, username):
        user = User.objects.get(username=username)
        received_movements = user.receiver.all()
        sent_movements = user.sender.all()
        user.movements = list(chain(received_movements, sent_movements))
        user.notifications = user.user_nots.all()
        user.vaults = user.user_vaults.all()
        return LoggedUserSerializer(user).data

    async def connect(self):
        self.group_name = self.scope['user']['username']

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name, {
                'type': 'user_data',
                'data': await self.get_user(self.scope['user']['username'])
            }
        )

        try:
            await self.channel_layer.group_send(
                data['username'], {
                    'type': 'user_data',
                    'data': await self.get_user(data['username'])
                }
            )
        except KeyError:
            pass

    async def user_data(self, event):
        data = event['data']
        await self.send(text_data=json.dumps({
            'data': data
        }))
