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
        selected_choice = choose.choice_set.get(pk=request.POST['search'])

    except(KeyError, choice.DoesNottExist):
        return render(request,'style.html',)
    else:
        selected_choice.compare +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result', args = (choose.id,)))

    @condition(selected_choice='Laptop')
    def front_page (request,blog_id):
        return HttpResponse('style2.html')

    @condition(selected_choice='Mobile Phone')
    def front_page (request,blog_id):
        return HttpResponse('style1.html')

