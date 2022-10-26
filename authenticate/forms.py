from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from app.models import Sponsor, Student, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['email', 'date_of_birth', 'full_name', 'city', 'address']
        widgets = {
            'date_of_birth': DateInput()
        }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match!")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
    
class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'date_of_birth', 'full_name', 'city', 'address', 'is_active', 'is_admin')
        
    def clean_password(self):
        return self.initial["password"]
    
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'full_name', 'city', 'address', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
        
# beta sponsor create (sign up)
class CustomSponsorCreation(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ('first_name', 'last_name', 'age', 'work_degree', 'students')

# beta student create (sign up)
class CustomStudentCreation(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('reason', 'first_name', 'last_name', 'phone_number', 'specification', 'email')