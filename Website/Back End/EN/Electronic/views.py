from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView,DeleteView
from .forms import CustomUserCreationForm
from .models import Product, Favorite
from django.contrib.auth.decorators import login_required


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProductView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'Electronic/details.html'


def productadded(request):
    return render(request, 'Electronic/add product.html')


def addProduct(request):
    prod = Product()
    prod.User = request.user
    prod.type = request.POST['type']
    prod.title = request.POST['title']
    prod.CPU = request.POST['cpu']
    prod.GPU = request.POST['gpu']
    prod.logo = request.POST['logo']
    prod.ram = request.POST['ram']
    prod.storage = request.POST['storage']
    prod.color = request.POST['color']
    prod.battery = request.POST['battery']
    prod.price = request.POST['price']
    prod.save()
    all_products = Product.objects.all()
    context = {'all_prod': all_products}
    return render(request, 'home.html', context)



def addFavorite(request, id):
    favo = Favorite()
    favo.customUser = request.user
    prod = Product.objects.get(pk=id)
    favo.product = prod
    favo.save()
    all_favo = Favorite.objects.all()
    context = {'all_favo': all_favo}
    return render(request, 'Electronic/favorite_list.html', context)


class ViewFavorite(generic.ListView):
    template_name = 'Electronic/favorite_list.html'
    context_object_name = 'all_favo'

    def get_queryset(self):
        return Favorite.objects.all()


def deletefav(request, id):
    fav = Favorite()
    fav = Favorite.objects.get(pk=id)
    fav.delete()
    all_favo = Favorite.objects.all()
    context = {'all_favo': all_favo}
    return render(request, 'Electronic/favorite_list.html', context)



class ADDNewProduct(generic.CreateView):
    model = Product
    fields = ['type', 'title', 'CPU', 'GPU', 'logo', 'ram', 'storage', 'color', 'battery', 'price']


class UpdateProduct(UpdateView):
    model = Product
    fields = ['type', 'title', 'CPU', 'GPU', 'logo', 'ram', 'storage', 'color', 'battery', 'price']
    success_url = reverse_lazy('home')


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('home')


def buildyourcomp(request):
    typo = request.POST['type']
    ram = request.POST['ram']
    cpu = request.POST['cpu']
    result = Product.objects.filter(CPU__contains=cpu, ram__contains=ram, type__contains=typo)
    return render(request, 'Electronic/buildyourcompresults.html', {'result': result})


def buildview(request):
    return render(request, 'Electronic/buildyourcomp.html')


@login_required
def profile(request):
    return render(request, 'Electronic/profile.html')

