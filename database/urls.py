"""urls configuration"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('get/', views.getComment, name='get'),
    path('tickets/', views.postComment, name='tickets'),
    path('ticket_review/', views.ticketReview, name='ticket_review'),
    path('follower/', views.follows_list, name='follower'),
    path('update_ticket/<str:pk>/', views.updateTicket, name='update_ticket'),
    path('update_review/<str:pk>/', views.updateReview, name='update_review'),
]
