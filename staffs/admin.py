# staffs/admin.py
from django.contrib import admin
from .models import Staff
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Staff)
class StaffAdmin(SimpleHistoryAdmin):
    list_display = ('full_name', 'email', 'phone', 'position', 'hire_date', 'is_active', 'created_at', 'updated_at')
    list_filter = ('position', 'hire_date', 'is_active')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('full_name',)
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone', 'position', 'hire_date', 'is_active')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
