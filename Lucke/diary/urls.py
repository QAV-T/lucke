from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('profile/', views.profile_view, name='profile'),
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
]
