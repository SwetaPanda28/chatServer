from typing import Container
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UsermodelSerializer
    queryset = User.objects.all()


class MsgViewSet(viewsets.ModelViewSet):
    serializer_class = MsgSerializer
    queryset = Message.objects.all()


def login(request):
    print("done")
    try:
        token, _ = Token.objects.get_or_create(user=request.user)
        return JsonResponse({"token": token.key})
    except:
        return render(request, "index.html")
