from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    template = loader.get_template('store/home.html')
    return HttpResponse(template.render(request=request))

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'store/register.html', context)
    
def loginPage(request):
    return HttpResponse('Please, login here')
