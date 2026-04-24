import json
from channels.generic.websocket import AsyncWebsocketConsumer
from user.models import UserModel   # или модель клиента, которую вы используете

class SearchConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'search_group'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        query = text_data_json['query']

        
        clients = UserModel.objects.filter(full_name__icontains=query)[:10]

       
       

        await self.send(text_data=json.dumps({
            'clients': clients
        }))