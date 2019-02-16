from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.ProductView.as_view(), name='home'),
    path('<int:pk>', views.ProductDetails.as_view(), name='detail'),
    path('favo/<int:id>', views.addFavorite, name='add_favorite'),
    path('favo/<int:id>/delete/', views.deletefav, name='delete_fav'),
    path('favo/', views.ViewFavorite.as_view(), name='favorite'),
    path('profile/', views.profile, name='profile'),
    path('addproduct/', views.productadded, name='addproduct'),
    path('addproduct/added/', views.addProduct, name='added'),
    path('addproduct/<int:pk>,', views.UpdateProduct.as_view(), name='edit'),
    path('addproduct/<int:pk>/delete', views.DeleteProduct.as_view(), name='delete'),
    path('build/', views.buildview, name='build'),
    path('build/result/', views.buildyourcomp, name='result'),
]

