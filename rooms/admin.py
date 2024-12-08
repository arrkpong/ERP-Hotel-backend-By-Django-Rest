# rooms/admin.py
from django.contrib import admin
from .models import Room, Amenity, RoomAmenity
from simple_history.admin import SimpleHistoryAdmin

class RoomAmenityInline(admin.TabularInline):
    model = RoomAmenity
    extra = 1

@admin.register(Room)
class RoomAdmin(SimpleHistoryAdmin):
    list_display = ('number', 'type', 'status', 'price_per_night', 'size', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('number', 'type')
    inlines = [RoomAmenityInline]
    ordering = ('number',)

@admin.register(Amenity)
class AmenityAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(RoomAmenity)
class RoomAmenityAdmin(SimpleHistoryAdmin):
    list_display = ('room', 'amenity', 'quantity')
    search_fields = ('room__number', 'amenity__name')
    ordering = ('room',)
