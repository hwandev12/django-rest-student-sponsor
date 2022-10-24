from django.contrib import admin
from django.urls import path, include
from authenticate.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', SignUpView.as_view())
]
