from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Electronic.urls')),
    path('users/', include('Electronic.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
