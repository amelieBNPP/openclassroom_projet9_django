from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CreateTicketForm, CreateUserForm, CreateReviewForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Ticket, UserFollows, Review
from django.contrib.auth.models import User
from operator import attrgetter


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
    print("loginPage")
    if request.method == "POST":
        print("valeur dans loginPage")
        print(request.POST)
        form = CreateUserForm(request.POST)
        print(form)
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
            Ticket.objects.get(
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
        return render(request, 'products/get.html', {'all_data': all_data})


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
                    pk=request.POST['sub-following-button']
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
            return redirect('products/get.html')
    return render(request, 'products/review.html', {'form': form})


@ login_required(login_url='login')
def updateTicket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = CreateTicketForm(instance=ticket)
    if request.method == "POST":
        form = CreateTicketForm(request.POST, request.FILES, instance=ticket)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('get')
    return render(request, 'update_ticket.html', {'form': form})


@ login_required(login_url='login')
def updateReview(request, pk):
    review = Review.objects.get(id=pk)
    ticket = Ticket.objects.get(id=review.ticket.id)
    form = CreateReviewForm(instance=review)
    if request.method == "POST":
        form = CreateReviewForm(request.POST, instance=review)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('get')
    return render(request, 'update_review.html', {'form': form, 'ticket': ticket, 'rating_range': range(6)})


@ login_required(login_url='login')
def ticketReview(request):
    form_ticket = CreateTicketForm()
    form_review = CreateReviewForm()
    if request.method == 'POST':
        form_ticket = CreateTicketForm({
            'title': request.POST['title'],
            'description': request.POST['description'],
        })

        if request.FILES:
            form_ticket.instance.image = request.FILES['image']
        form_ticket.instance.user = request.user

        form_review = CreateReviewForm({
            'headline': request.POST['headline'],
            'rating': request.POST['rating'],
            'body': request.POST['body'],
        })
        form_review.instance.user = request.user
        if all([form_ticket.is_valid(), form_review.is_valid()]):
            form_ticket.instance.reviewed = True
            form_ticket.save()
            form_review.instance.ticket = Ticket.objects.last()
            form_review.save()
        return redirect('get')
    return render(request, 'products/ticket_review.html', {'form_ticket': form_ticket, 'form_review': form_review, 'rating_range': range(6)})
