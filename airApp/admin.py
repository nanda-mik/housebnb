from django.contrib import admin

from .models import User, House, HouseType
# Register your models here.

admin.site.register(User)
admin.site.register(House)
admin.site.register(HouseType)