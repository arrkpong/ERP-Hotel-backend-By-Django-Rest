from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'booking', 
        'payment_method', 
        'amount', 
        'status', 
        'transaction_id', 
        'created_at'
    )
    search_fields = ('booking__guest__user__username', 'transaction_id')
    list_filter = ('status', 'payment_method', 'created_at')
