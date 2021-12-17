from typing import Container
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class=UserModel
    queryset=User.objects.all()


class MsgViewSet(viewsets.ModelViewSet):
    serializer_class=Msg
    queryset=User.objects.all()
