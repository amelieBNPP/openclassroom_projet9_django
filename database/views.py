from django import template
from django.contrib import auth
from django.db.models import fields
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
from django.contrib.auth.models import User
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
def follows_list(request):
    all_followers = []
    all_followed = []
    if UserFollows.objects.filter(user=request.user):
        for followed in UserFollows.objects.filter(user=request.user):
            all_followers.append(followed.followed_user)
    if UserFollows.objects.filter(followed_user=request.user):
        for flwing in UserFollows.objects.filter(followed_user=request.user):
            all_followed.append(flwing.user)
    all_users = User.objects.all()
    if request.method == 'GET':
        context = {
            'all_followers': all_followers,
            'all_followed': all_followed,
            'all_users': all_users,
        }
        return render(request, 'products/follower.html', context)
    if request.method == 'POST':
        if request.POST.get('followed_user'):
            UserFollows(
                user=request.user,
                followed_user=User.objects.get(
                    pk=request.POST['followed_user']
                )
            ).save()
        if request.POST.get('remove_from_followers'):
            UserFollows.objects.get(
                user=request.user,
                followed_user=User.objects.get(
                    id=request.POST['remove_from_followers']
                ),
            ).delete()
        return redirect('follower')
