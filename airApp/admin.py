from django.contrib import admin

from .models import User, House, HouseType
# Register your models here.

myModels = [User, House, HouseType]

admin.site.register(myModels)