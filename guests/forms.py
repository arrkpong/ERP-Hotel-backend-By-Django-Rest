# guests/forms.py
from django import forms
from .models import Guest

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['full_name', 'email', 'phone', 'id_card_number', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your address'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'id_card_number': forms.TextInput(attrs={'placeholder': 'Enter ID card number'}),
        }
