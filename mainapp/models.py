from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    pu = models.TextField()
    pr = models.TextField()
    dp = models.ImageField()
    nprod = models.TextField()


class Message(models.Model):
    text = models.TextField()
    id = models.UUIDField(default=uuid4, primary_key=True)
    touser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recieved_messages", null=True
    )
    fromuser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages", null=True
    )


class Image(models.Model):
    img = models.ImageField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
