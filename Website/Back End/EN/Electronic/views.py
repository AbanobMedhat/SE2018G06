from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import Product


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.


class ProductView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'Electronic/details.html'
