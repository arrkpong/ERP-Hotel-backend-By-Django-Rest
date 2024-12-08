# bookings/forms.py
from django import forms
from .models import Booking, Payment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'room', 'check_in', 'check_out', 'cancellation_fee', 'refundable']
        widgets = {
            'guest': forms.Select(attrs={'placeholder': 'Select a guest'}),
            'room': forms.Select(attrs={'placeholder': 'Select a room'}),
            'check_in': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Choose check-in date'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Choose check-out date'}),
            'cancellation_fee': forms.NumberInput(attrs={'placeholder': 'Enter cancellation fee'}),
            'refundable': forms.CheckboxInput(attrs={'placeholder': 'Refundable'}),
        }
    
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'amount_paid']
