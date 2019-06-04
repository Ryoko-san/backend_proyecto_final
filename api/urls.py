from django.contrib import admin
from django.urls import path, include
from api import views, views_2

urlpatterns = [
    path('users/<int:id>', views.UsersView.as_view(), name='Users_id'),
    path('users/', views.UsersView.as_view(), name='Users_id'),
    path('shifts/', views_2.ShiftsView.as_view(), name='Shifts'),
    path('shifts/<int:id>', views_2.ShiftsView.as_view(), name='Shifts_id'),
    path('shifts/<str:date>', views_2.ShiftsView.as_view(), name='Shifts_id'),
    path('shift-types/', views_2.ShiftTypesView.as_view(), name='Shift_type'),
    path('shifts/user/<str:date>', views.ShiftViews.as_view(), name='Shifts_id')
]
