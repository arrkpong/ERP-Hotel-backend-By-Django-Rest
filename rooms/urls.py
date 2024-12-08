# rooms/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:pk>/', views.room_detail, name='room_detail'),
    path('rooms/new/', views.room_create, name='room_create'),
    path('rooms/<int:pk>/edit/', views.room_edit, name='room_edit'),
    path('rooms/<int:pk>/delete/', views.room_delete, name='room_delete'),
    
    path('amenitis/', views.amenity_list, name='amenity_list'),
    path('amenitys/<int:pk>/', views.amenity_detail, name='amenity_detail'),
    path('amenitys/new/', views.amenity_create, name='amenity_create'),
    path('amenitys/<int:pk>/edit/', views.amenity_edit, name='amenity_edit'),
    path('amenitys/<int:pk>/delete/', views.amenity_delete, name='amenity_delete'),
]
