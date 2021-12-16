from django.contrib import admin

from mainapp.models import Msg, UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Msg)