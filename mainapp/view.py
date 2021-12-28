from typing import Container
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class=UsermodelSerializer
    queryset=User.objects.all()


class MsgViewSet(viewsets.ModelViewSet):
    serializer_class=MsgSerializer
    queryset=Msg.objects.all()
