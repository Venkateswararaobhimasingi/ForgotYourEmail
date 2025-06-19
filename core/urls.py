from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_login, name='login'),
    path('register/', views.custom_register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.custom_logout, name='logout'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),

]