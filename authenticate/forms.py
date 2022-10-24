from django import forms
from django.contrib.auth import get_user_model
from app.models import Sponsor
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", 'email')
    
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")
        
class CustomSponsorCreation(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ('first_name', 'last_name', 'age', 'work_degree', 'students')