from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.ProductView.as_view(), name='home'),
    path('<int:pk>', views.ProductDetails.as_view(), name='detail'),
]
