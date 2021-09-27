from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.db.models import fields
from django.db.models.fields import TextField
from django.contrib.auth.models import AbstractUser
from django.forms import widgets


class Ticket(models.Model):
    # Your Ticket model definition goes here
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
    )
    time_created = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    ticket = models.ForeignKey(
        to=Ticket,
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by',
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user',)

    # def __str__(self):
    #     return f'{self.user} follows {self.followed_user}'
