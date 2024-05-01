from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('weather/', views.weather, name='weather'),
    path('logout/', views.custom_logout, name='logout'),
]
