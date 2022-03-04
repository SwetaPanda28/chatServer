from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import *

class UsermodelSerializer(ModelSerializer):#convert models to json+ its has many features such as read only fields
    class Meta:
        model = User
        fields = '__all__'


class MsgSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__' 

