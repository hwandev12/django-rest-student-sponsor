from django.shortcuts import render, reverse, redirect
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomSponsorCreation, CustomStudentCreation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def entry(request):
    return render(request, 'pages/home.html')

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


def userLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, password=password, email=email)
        
        if user is not None:
            form = login(request, user)
            messages.success(request, f"Welcome again!")
            return redirect('/')
        else:
            messages.info(request, 'First name or Email is not matching!')
            return redirect('/')
    
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})