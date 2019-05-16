from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('users/<int:id>', views.UsersView.as_view(), name='Users_id'),
    path('users/', views.UsersView.as_view(), name='Users_id'),
    path('contacts/', views.UsersView.as_view(), name='all-contacts'),
]
