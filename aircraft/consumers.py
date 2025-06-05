from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AircraftConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("aircraft_updates", self.channel_name)
        await self.accept()
        print("🧲 Cliente WebSocket conectado:", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("aircraft_updates", self.channel_name)

    async def receive(self, text_data):
        # Solo para test
        await self.send(text_data=json.dumps({"message": "Conectado"}))

    async def aircraft_event(self, event):
        print("📨 Enviando mensaje al cliente WebSocket")
        await self.send(text_data=json.dumps(event["content"]))
