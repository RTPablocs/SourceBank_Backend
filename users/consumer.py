import json
from channels.generic.websocket import AsyncWebsocketConsumer
from users.serializers import LoggedUserSerializer


class UserConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        await self.accept()

    def disconnect(self, code):
        pass

    async def websocket_receive(self, message):

        serializer = LoggedUserSerializer(self.scope['user'])
        await self.send(json.dumps({
            'user': self.scope['user']
        }, ensure_ascii=False))
