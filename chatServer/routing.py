from django.urls import path
from mainapp import consumers

url_patterns = [
    path("messenger", consumers.Messenger.as_asgi(), name="messenger"),
]
