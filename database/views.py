from django import template
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def home(request):
    template = loader.get_template('accounts/home.html')
    return HttpResponse(template.render(request=request))


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
