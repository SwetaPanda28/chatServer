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
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    img = models.ImageField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
