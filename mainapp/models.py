from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField


class UserModel(models.Model):
    privateKey=models.CharField(max_length=100,blank=True)
    publicKey=models.CharField(max_length=100,blank=True)
    masterpassword=models.CharField(max_length=100,blank=True)
    image_field = models.ImageField(null=True,blank=True)
    phoneNumber = PhoneNumberField(unique = True, null = True,blank=True)
    authUser = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    detailsFilled=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f"{self.authUser.email} : {self.authUser.username}"

class Msg(models.Model):
    msg=models.CharField(max_length=10000)
    sender=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="sender")
    receiver=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="reciever")
        
    
