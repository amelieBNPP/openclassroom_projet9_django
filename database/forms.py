from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import forms, CharField, ImageField, ModelForm
from .models import Ticket, UserFollows, Review


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
        # widgets = {'rating': ModelForm.NumberInput(attrs={'class': 'Stars'})}
        # labels = {'rating': 'Note /5'}
