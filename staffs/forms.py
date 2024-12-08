# staffs/forms.py
from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'email', 'phone', 'position', 'hire_date', 'is_active']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'hire_date': forms.DateInput(attrs={'placeholder': 'Select hire date', 'type': 'date'}),
            'is_active': forms.CheckboxInput(),
        }
