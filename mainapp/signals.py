from django.dispatch import receiver
from django.db.models.signals import post_save
from . import models
from channels.consumer import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


@receiver(post_save, sender=models.Message)
def sendLatestMessage(sender, instance: models.Message, **kwargs):
    room_name = "main"

    async_to_sync(channel_layer.group_send)(
        room_name, {"type": "chat.message", "message": instance.text}
    )
    print("message sent")
