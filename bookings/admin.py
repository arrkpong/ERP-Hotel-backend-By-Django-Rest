# bookings/admin.py
from django.contrib import admin
from .models import Booking, Payment
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Booking)
class BookingAdmin(SimpleHistoryAdmin):
    list_display = ('guest', 'room', 'check_in', 'check_out', 'cancellation_fee', 'refundable', 'created_at', 'updated_at')
    list_filter = ('check_in', 'check_out', 'room', 'guest')
    search_fields = ('guest__full_name', 'room__room_number')  # Assuming 'full_name' and 'room_number' are fields in Guest and Room models
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('guest', 'room', 'check_in', 'check_out', 'cancellation_fee', 'refundable')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Payment)
class PaymentAdmin(SimpleHistoryAdmin):
    list_display = ('booking', 'payment_method', 'amount_paid', 'payment_date')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('booking__id',)
    ordering = ('-payment_date',)
    fieldsets = (
        (None, {'fields': ('booking', 'payment_method', 'amount_paid')}),
        ('Timestamps', {'fields': ('payment_date',)}),
    )
    readonly_fields = ('payment_date',)
