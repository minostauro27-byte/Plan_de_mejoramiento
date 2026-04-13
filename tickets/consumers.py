from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AlertConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("🔥 WebSocket conectado")
        await self.channel_layer.group_add("alertas", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("alertas", self.channel_name)

    async def enviar_alerta(self, event):
        await self.send(text_data=json.dumps(event["message"]))