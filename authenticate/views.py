from django.shortcuts import render, reverse, redirect
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomSponsorCreation, CustomStudentCreation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

class SignUpView(CreateView):
    form_class = CustomSponsorCreation
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse('home')

def customStudentSignup(request):
    if request.method == 'POST':
        form = CustomStudentCreation(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.owner = request.user
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f"Account was created for {first_name}")
            messages.add_message(request, messages.INFO, 'You can change it later')
            student.save()
            return redirect('/')
    else:
        form = CustomStudentCreation()
    return render(request, 'registration/student.html', {'form': form})


def customStudentLogin(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        email = request.POST['email']
        
        user = authenticate(request, first_name=first_name, email=email)
        
        if user is not None:
            form = login(request, user)
            messages.success(request, f"Welcome {first_name} again!")
            return redirect('/')
        else:
            messages.info(request, 'First name or Email is not matching!')
            return redirect('/')
    
    form = AuthenticationForm()
    return render(request, 'registration/student-login.html', {"form": form})