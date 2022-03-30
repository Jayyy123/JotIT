from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutPage, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/<str:pk>/', views.logoutPage, name='edit_profile'),
]