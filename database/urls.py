"""urls configuration"""

from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('get/', views.getComment, name='get'),
    path('tickets/', views.postComment, name='tickets'),
    path('follower/', views.follows_list, name='follower'),
    path('update_ticket/', views.updateTicket, name='update_ticket'),
    path('delete_ticket/', views.deleteTicket, name='delete_ticket'),
    # path('error/', views.error, name='404'),
    # path('blank/', views.blank, name='blank'),
]
