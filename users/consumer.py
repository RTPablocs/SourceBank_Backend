import json
from channels.generic.websocket import AsyncWebsocketConsumer
from users.serializers import LoggedUserSerializer
from asgiref.sync import async_to_sync


class UserConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            self.scope['user']['username'],
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.scope['token'],
            self.channel_name
        )

    async def websocket_receive(self, text_data):
        await self.channel_layer.group_send(
            self.scope['user']['username'], {
                'type': 'user_data',
                'data': self.scope['user']
            }
        )

    async def user_data(self, event):
        data = event['data']
        await self.send(text_data=json.dumps({
            'data': data
        }))
