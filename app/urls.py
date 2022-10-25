from django import views
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'users', UserViewSet, basename='users')
router.register(r'sponsors', SponsorViewSet, basename='sponsors')
router.register(r'filter-user-list', FilterPerUserProduction, basename='filter')

app_name = 'app'

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home')
]