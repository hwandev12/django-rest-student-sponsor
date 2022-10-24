from django.contrib import admin
from django.contrib.auth import get_user_model
from authenticate.forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'is_super', 'is_user', 'is_agent']

admin.site.register(User, CustomUserAdmin)
