from django import template
from django.contrib import auth
from django.db.models import fields, Value
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateTicketForm, CreateUserForm, CreateReviewForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Ticket, UserFollows, Review
from django.contrib.auth.models import User
from operator import attrgetter

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
            return redirect('get')
        else:
            messages.info(request, 'username or password is incorrect')
    return render(request, 'accounts/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def getComment(request):
    print("getcomment..........")
    if request.method == 'POST':
        if request.POST.get('sub-ask-review-button'):
            ticket_review = Ticket.objects.get(
                id=request.POST['sub-ask-review-button']
            )
            form_review = CreateReviewForm()
            return render(
                request,
                'products/reviews.html',
                {
                    'ticket_review': ticket_review,
                    'form_review': form_review,
                    'rating_range': range(6),
                },

            )
        if request.POST.get('delete-ticket-button'):
            test = Ticket.objects.get(
                user=request.user,
                id=request.POST['delete-ticket-button']
            ).delete()

        if request.POST.get('delete-review-button'):
            Review.objects.get(
                user=request.user,
                id=request.POST['delete-review-button']
            ).delete()

        if request.POST.get('sub-send-review-button'):
            form_review = CreateReviewForm(request.POST)
            form_review.instance.user = request.user
            form_review.instance.ticket = Ticket.objects.get(
                id=request.POST['sub-send-review-button']
            )
            if form_review.is_valid():
                form_review.save()
                Ticket.objects.filter(
                    id=request.POST['sub-send-review-button']
                ).update(reviewed=True)
            headline = form_review.cleaned_data.get('headline')
        return redirect('get')
    if request.method == 'GET':
        followed_users = [object.followed_user
                          for object in UserFollows.objects.all()
                          if object.user == request.user]
        tickets_to_review = [
            ticket for ticket in list(Ticket.objects.filter(reviewed=False))
            if (ticket.user in followed_users)
            or (ticket.user == request.user)
        ]
        tickets_reviewed = [
            ticket for ticket in list(Review.objects.all())
            if (ticket.user in followed_users)
            or (ticket.user == request.user)
        ]
        all_data = tickets_to_review + tickets_reviewed
        all_data.sort(key=attrgetter('time_created'), reverse=True)
        return render(request, 'products/get.html', {'all_data': all_data, 'range_rate': range(5)})


@ login_required(login_url='login')
def postComment(request):
    form_post_comment = CreateTicketForm()
    if request.method == "POST":
        form_post_comment = CreateTicketForm(request.POST)
        form_post_comment.instance.user = request.user
        if request.FILES:
            form_post_comment.instance.image = request.FILES['image']
        if form_post_comment.is_valid():
            form_post_comment.save()
            title = form_post_comment.cleaned_data.get('title')
            messages.success(
                request, f'information regarding your book, {title} has been saved')
            return redirect('get')
        else:
            form_post_comment = CreateTicketForm()
    return render(request, 'products/tickets.html', {'form_post_comment': form_post_comment})


@ login_required(login_url='login')
def follows_list(request):
    all_followers = []
    all_followed = []
    if UserFollows.objects.filter(user=request.user):
        for followed in UserFollows.objects.filter(user=request.user):
            all_followers.append(followed.followed_user)
    if UserFollows.objects.filter(followed_user=request.user):
        for flwing in UserFollows.objects.filter(followed_user=request.user):
            all_followed.append(flwing.user)
    all_users = set(User.objects.all()) - set(all_followers)
    if request.method == 'GET':
        context = {
            'all_followers': all_followers,
            'all_followed': all_followed,
            'all_users': all_users,
        }
        return render(request, 'products/follower.html', context)
    if request.method == 'POST':
        if request.POST.get('sub-new-following'):
            UserFollows(
                user=request.user,
                followed_user=User.objects.get(
                    pk=request.POST['sub-new-following']
                )
            ).save()
        if request.POST.get('sub-following-button'):
            UserFollows.objects.get(
                user=request.user,
                followed_user=User.objects.get(
                    id=request.POST['sub-following-button']
                ),
            ).delete()
        return redirect('follower')


@ login_required(login_url='login')
def review_page(request):
    form = CreateReviewForm()
    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(
                request, f'information regarding your book, has been saved')
            return redirect('products/get.html')
    return render(request, 'products/review.html', {'form': form})


def updateTicket(request):
    template = loader.get_template('/update_ticket.html')
    return HttpResponse(template.render(request=request))


def error(request):
    template = loader.get_template('/404.html')
    return HttpResponse(template.render(request=request))


def blank(request):
    template = loader.get_template('/blank.html')
    return HttpResponse(template.render(request=request))
