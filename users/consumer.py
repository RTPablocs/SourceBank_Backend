import json
from channels.generic.websocket import AsyncWebsocketConsumer
from users.serializers import LoggedUserSerializer


class UserConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        await self.accept()

    def disconnect(self, code):
        pass

    async def websocket_receive(self, message):
        print(self.scope)
        serializer = LoggedUserSerializer(self.scope['user'])
        await self.send(text_data=json.dumps({
            'message': serializer.data
        }))
