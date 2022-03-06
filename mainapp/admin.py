from django.contrib import admin

from mainapp.models import Message, User, Image

# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Image)
