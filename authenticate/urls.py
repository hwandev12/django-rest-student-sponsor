from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .views import customStudentSignup, SignUpView, customStudentLogin

app_name = 'authenticate'

urlpatterns = [
    path('student-sign/', customStudentSignup, name='student-sign'),
    path('student-login/', customStudentLogin, name='student-login'),
]
