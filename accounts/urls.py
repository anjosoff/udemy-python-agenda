from django.urls import path 
from . import views

urlpatterns = [
    path('', views.login, name='index_login.html'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
