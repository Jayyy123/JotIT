from django.urls import path
from . import views

urlpatterns = [
    path('', views.jotters, name='jotters'),
    path('/add_jotter/', views.add_jotters, name='add_jotter'),
    path('/edit_jotter/', views.edit_jotters, name='edit_jotter'),
]