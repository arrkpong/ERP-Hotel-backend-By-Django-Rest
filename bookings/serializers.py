from rest_framework import serializers
from .models import Payment
from bookings.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'guest', 'room', 'check_in_date', 'check_out_date', 'total_price']

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()

    class Meta:
        model = Payment
        fields = [
            'id', 
            'booking', 
            'payment_method', 
            'amount', 
            'status', 
            'transaction_id', 
            'created_at'
        ]
