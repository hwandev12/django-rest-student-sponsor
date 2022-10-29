from django.shortcuts import render, reverse, redirect
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomSponsorCreation, CustomStudentCreation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.conf import settings


def entry(request):
    if not request.user.is_authenticated:
        return render(request, 'pages/404.html')
    return render(request, 'pages/authentication.html')


def userSignup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            messages.success(
                request, f"Account successfully created for {first_name}", extra_tags='suc-sign')
            user.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# @login_required(login_url='/authentication/login/')
def customStudentEnroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login or register to continue!", extra_tags='aut-warning')
        return redirect('/authentication/login/')
    if request.method == 'POST':
        form = CustomStudentCreation(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.owner = request.user
            first_name = form.cleaned_data.get('first_name')
            messages.success(
                request, f"Enroll successfully submitted for {first_name}", extra_tags='success')
            messages.add_message(request, messages.INFO,
                                 'You can change it later', extra_tags='info')
            student.save()
            return redirect('/authentication/')
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
            full_name = user.full_name
            messages.success(request, f"Welcome {full_name} again!", extra_tags='login')
            return redirect('/')
        else:
            messages.info(request, 'First name or Email is not matching!')
            return redirect('/')

    form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form": form})

def logout_view(request):
    logout(request)
    messages.warning(request, f"You are logged out!", extra_tags='logout')
    return redirect('/')

def logout_sample(request):
    return render(request, 'pages/logout.html')

# customSponsorCreation
# @login_required(login_url='/authentication/login/')
def customSponsorCreation(request): 
    if not request.user.is_authenticated:
        messages.warning(request, "Please login or register to continue!", extra_tags='aut-warning')
        return redirect('/authentication/login/')
    if request.method == 'POST':
        form = CustomSponsorCreation(request.POST)
        if form.is_valid():
            sponsor = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f"Successfully submitted for {first_name}", extra_tags='sponsor-enroll')
            sponsor.save()
            return redirect('/')
    else:
        form = CustomSponsorCreation()
    return render(request, 'registration/sponsor-enroll.html', {"form": form})