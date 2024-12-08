# guests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('guests/', views.guest_list, name='guest_list'),
    path('guests/<int:pk>/', views.guest_detail, name='guest_detail'),
    path('guests/new/', views.guest_create, name='guest_create'),
    path('guests/<int:pk>/edit/', views.guest_edit, name='guest_edit'),
    path('guests/<int:pk>/delete/', views.guest_delete, name='guest_delete'),
]
