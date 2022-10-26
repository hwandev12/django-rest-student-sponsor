from django.contrib import admin
from django.urls import path, include
from authenticate.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('signup/', include('authenticate.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
