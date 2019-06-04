from django.contrib import admin
from django.urls import path, include
from api import views, views_2

urlpatterns = [
    path('users/', views.UsersView.as_view(), name='users'),
    path('users/<int:id>', views.UsersView.as_view(), name='users_id'),
    path('shifts/', views_2.ShiftsView.as_view(), name='shifts'),
    path('shifts/<int:id>', views_2.ShiftsView.as_view(), name='shifts_id'),
    path('shifts/<str:date>', views_2.ShiftsView.as_view(), name='shifts_date'),
    path('shifts-types/', views_2.ShiftTypesView.as_view(), name='shifts_type'),
    path('shifts-types/<int:id>', views_2.ShiftTypesView.as_view(), name='shifts_type_id'),
    path('positions/', views_2.PositionsView.as_view(), name='positions'),
    path('positions/<int:id>', views_2.PositionsView.as_view(), name='positions_id'),
    path('shifts/user/<str:date>', views.ShiftViews.as_view(), name='Shifts_id')
]
