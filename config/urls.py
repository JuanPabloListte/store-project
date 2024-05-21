from django.contrib import admin
from django.urls import path, include
from apps.homepage.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('apps.core.urls')),
    path('', HomeView.as_view(), name='home'),
    path('login/', include('apps.login.urls')),
]
