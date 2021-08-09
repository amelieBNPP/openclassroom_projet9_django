"""urls configuration"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('get/', views.getComment, name='get'),
    path('post/', views.postComment, name='post'),
]
