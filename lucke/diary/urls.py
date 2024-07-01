from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('newdiary/', views.create_diary, name='create_diary'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('logout_confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('profile/', views.profile_view, name='profile'),
    path('diary/<int:diary_id>/', views.diary_detail, name='diary_detail'),
    path('diary/<int:diary_id>/edit/', views.diary_edit, name='diary_edit'),
    path('diary/<int:diary_id>/delete/', views.diary_delete, name='diary_delete'),
]