from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .views import customStudentSignup, SignUpView, userLogin, entry

app_name = 'authenticate'

urlpatterns = [
    path('', entry, name='home'),
    path('student-sign/', customStudentSignup, name='student-sign'),
    path('login/', userLogin, name='login'),
]
