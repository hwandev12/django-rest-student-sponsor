from django.contrib import admin
from django.urls import path, include
from authenticate.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('authentication/', include('authenticate.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
