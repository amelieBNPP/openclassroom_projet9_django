from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Ticket, Review


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
