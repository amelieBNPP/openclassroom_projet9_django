from django import template
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateTicketForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Ticket, UserFollows

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


@login_required(login_url='login')
def getComment(request):
    all_tickets = Ticket.objects.all()
    return render(request, 'products/get.html', {'all_tickets': all_tickets})


@login_required(login_url='login')
def postComment(request):
    form = CreateTicketForm()
    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(
                request, f'information regarding your book, {title} has been saved')
            return redirect('products/get.html')
    return render(request, 'products/post.html', {'form': form})


@login_required(login_url='login')
def following(request):
    all_followers = UserFollows.objects.all()
    return render(request, 'products/follower.html', {'all_followers': all_followers})


@login_required(login_url='login')
def followedBy(request):
    all_followed = UserFollows.objects.all()
    return render(request, 'products/follower.html', {'all_followed': all_followed})


# @login_required(login_url='login')
# def addFollowing(request):
#     form = UserFollows()
#     if request.method == "POST":
#         form = UserFollows(request.POST)
#         form.instance.username = ['user1', 'user2', 'user3']
#     all_followed = UserFollows.objects.filter(followed_user=request.user)
#     return render(request, 'products/follower.html', {'all_followed': all_followed})
