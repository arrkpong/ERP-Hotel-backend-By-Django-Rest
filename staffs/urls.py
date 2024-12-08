# staffs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('staffs/', views.staff_list, name='staff_list'),
    path('staffs/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staffs/new/', views.staff_create, name='staff_create'),
    path('staffs/<int:pk>/edit/', views.staff_edit, name='staff_edit'),
    path('staffs/<int:pk>/delete/', views.staff_delete, name='staff_delete'),
]
