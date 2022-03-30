from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='overview'),
    # path('user-login/', views.user-login, name='user-login'),
    # path('user-signup/', views.user-signup, name='user-signup'),
    # path('user-logout/', views.user-logout, name='user-logout'),
    # path('user-profile/', views.user-profile, name='user-profile'),
    # path('profile-update/<str:pk>/', views.profile-update, name='profile-update'),
    # path('profile-create/', views.profile-create, name='profile-create'),
    # path('profile-delete/<str:pk>/', views.profile-delete, name='profile-delete'),
    path('jotters/', views.jotters, name='all-jotters'),
    path('jotter/<str:pk>/', views.jotter, name='single-jotter'),
    path('add-jotter/', views.add_jotter, name='add-jotter'),
    path('edit-jotter/<str:pk>/', views.edit_jotter, name='edit-jotter'),
    path('delete-jotter/<str:pk>/', views.delete_jotter, name='delete-jotter'),
]