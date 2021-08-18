from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import forms, CharField, ImageField, ModelForm
from .models import Ticket


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


# class CreateUserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username']
