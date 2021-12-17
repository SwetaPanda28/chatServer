from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import *

class UsermodelSerializer(ModelSerializer):#convert models to json+ its has many features such as read only fields
    class Meta:
        model = UserModel
        fields = '__all__'


class MsgSerializer(ModelSerializer):
    class Meta:
        model = Msg
        fields = '__all__' 

