# notice_board_app/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NoticeBoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        message = json.loads(text_data)
        content = message['content']

        # Save the message to the database
        # You need to import the Message model from models.py
        # from .models import Message
        # Message.objects.create(content=content)

        # Broadcast the message to all connected clients
        await self.send(text_data=json.dumps({
            'content': content,
            'created_at': 'Just Now',  # You can modify this based on your requirements
        }))
