from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import CustomUser, Student, Sponsor, SponsoredStudents
from django import forms

class SponsorForm(forms.ModelForm):
    model = Sponsor
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('students').count() >= 10:
            raise ValidationError('You have to choose exactly 10 students only!')

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    form = SponsorForm

admin.site.register(Student)
admin.site.register(SponsoredStudents)
