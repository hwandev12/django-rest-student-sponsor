from django.urls import path
from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

import random
mix = random.randint(100000000000,999999999999)

app_name = 'authenticate'

urlpatterns = [
    re_path(r'^$', entry, name='home'),
    path('student-sign/', customStudentEnroll, name='student-sign'),
    path('sponsor-sign/', customSponsorCreation, name='sponsor-sign'),
    path('login/', userLogin, name='login'),
    path('signup/', userSignup, name='signup'),
    path('mix/', logout_view, name='logout'),
    re_path(r'^logout/', logout_sample, name='logout-sam')
]
