from django.views.generic import TemplateView
from django.shortcuts import render
from Build.forms import HomeForm
from django.db.models import When


class HomeView (TemplateView):
    template_name = 'build.html'

    def get(self, request):
        form = HomeForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request ):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            Device_Type = request.POST.get('type','')
            RAM = request.POST.get('ram','')
            CPU = request.POST.get('cpu','')
            internal_storage =request.POST.get('harddisk','')
            VGA = request.POST.get('vga','')

        When(Device_Type='Lab', RAM='2GB', CPU='Intel core i5', then=self.front_page())


        args = {'form':form,'text': text}
        return render(request, self.template_name, args)
    def front_page(self):
        html = "<html> <body> \"<img src= \"5.jpg\"> </body></html>"

