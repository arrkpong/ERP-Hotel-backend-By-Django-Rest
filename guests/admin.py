# guests/admin.py
from django.contrib import admin
from .models import Guest
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Guest)
class GuestAdmin(SimpleHistoryAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('created_at', 'updated_at')
    ordering = ('full_name',)
