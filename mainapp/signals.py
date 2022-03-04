from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . import models

@receiver(post_save,sender=User)
def createUserModel(instance,created,**kwargs):
    if(created):
        models.User.objects.create(authUser=instance)
