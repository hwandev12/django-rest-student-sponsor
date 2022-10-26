from django.contrib import admin
from django.contrib.auth.models import Group
from .forms import UserAdmin
from app.models import CustomUser

admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
