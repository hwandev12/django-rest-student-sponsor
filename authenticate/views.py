from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomSponsorCreation

class SignUpView(CreateView):
    form_class = CustomSponsorCreation
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse('home')
