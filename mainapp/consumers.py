from channels.consumer import AsyncConsumer


class Messenger(AsyncConsumer):
    async def websocket_connect(self):
        self.accept
