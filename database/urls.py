"""urls configuration"""

from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('get/', views.getComment, name='get'),
    path('post/', views.postComment, name='post'),
    path('follower/', views.follows_list, name='follower'),
    # path('error/', views.error, name='404'),
    # path('blank/', views.blank, name='blank'),
]
