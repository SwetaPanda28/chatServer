from channels.consumer import AsyncConsumer, database_sync_to_async, async_to_sync


class Messenger(AsyncConsumer):
    async def websocket_connect(self, event):
        room_name = "main"
        await self.channel_layer.group_add(room_name, self.channel_name)
        await self.send({"type": "websocket.accept"})

    async def websocket_disconnect(self, event):

        await self.send({"type": "websocket.close"})

    async def chat_message(self, event):
        message = event["message"]
        await self.send({"type": "websocket.send", "text": message})
