from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('subjects/', TemplateView.as_view(template_name='subjects.html'), name='subjects'),
    path('s1/', TemplateView.as_view(template_name='s1.html'), name='s1'),
    path('s2/', TemplateView.as_view(template_name='s2.html'), name='s2'),
    path('s3/', TemplateView.as_view(template_name='s3.html'), name='s3'),
    path('users/', include('Electronic.urls')),
    path('users/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)