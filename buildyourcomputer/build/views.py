from django.core.files import images
from django.http import HttpResponse , HttpResponseRedirect
from django.views.decorators.http import condition
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404 , render
from .models import choice

def compare(request , question_id):
    choose = get_object_or_404(choice,pk=question_id)
    try:
        selected_choice = choose.choice_set.get(pk=request.POST['nope'])
        selected_choice1 = choose.choice_set.get(pk=request.POST['yes'])
        selected_choice2 = choose.choice_set.get(pk=request.POST['data'])
        selected_choice3 = choose.choice_set.get(pk=request.POST['ahmed'])
        selected_choice4 = choose.choice_set.get(pk=request.POST['get'])

    except(KeyError, choice.DoesNottExist):
        return render(request,'style.html',)
    else:
        selected_choice.compare +=1
        selected_choice1.compare += 1
        selected_choice2.compare += 1
        selected_choice3.compare += 1
        selected_choice4.compare += 1
        selected_choice.save()
        selected_choice1.save()
        selected_choice2.save()
        selected_choice3.save()
        selected_choice4.save()
        return HttpResponseRedirect(reverse('result', args = (choose.id,)))

    @condition(selected_choice='Laptop')
    @condition(selected_choice1='1GB')
    @condition(selected_choice2='Quad-core')
    @condition(selected_choice3='8GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Laptop')
    @condition(selected_choice1='2GB')
    @condition(selected_choice2='Octa-core')
    @condition(selected_choice3='8GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops1.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Laptop')
    @condition(selected_choice1='3GB')
    @condition(selected_choice2='AMD E-Series')
    @condition(selected_choice3='16GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops2.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Laptop')
    @condition(selected_choice1='4GB')
    @condition(selected_choice2='intel Core i7')
    @condition(selected_choice3='16GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops3.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Laptop')
    @condition(selected_choice1='8GB')
    @condition(selected_choice2='intel Core i3')
    @condition(selected_choice3='64GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops4.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Mobile Phone')
    @condition(selected_choice1='2GB')
    @condition(selected_choice2='Quad-core')
    @condition(selected_choice3='8GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Mobile Phone')
    @condition(selected_choice1='4GB')
    @condition(selected_choice2='Octa-core')
    @condition(selected_choice3='8GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Mobile Phone')
    @condition(selected_choice1='8GB')
    @condition(selected_choice2='AMD E-Series')
    @condition(selected_choice3='64GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops.jpg" style="float:right;height:60%">"</body></html>"


    @condition(selected_choice='Mobile Phone')
    @condition(selected_choice1='16GB')
    @condition(selected_choice2='intel Core i7')
    @condition(selected_choice3='16GB')
    def front_page (request,blog_id):
       html = "<html><body> <img src= ""images/laptops.jpg" style="float:right;height:60%">"</body></html>"


