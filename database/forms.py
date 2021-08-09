from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateTicketForm(UserCreationForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'Image']
