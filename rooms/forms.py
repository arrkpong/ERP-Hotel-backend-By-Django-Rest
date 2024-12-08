from django import forms
from .models import Room, Amenity

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'type', 'status', 'price_per_night', 'size', 'amenities']
        widgets = {
            'number': forms.TextInput(attrs={'placeholder': 'Enter room number (e.g. 101, 102)'}),
            'type': forms.TextInput(attrs={'placeholder': 'Enter room type (e.g. Single, Double, Suite)'}),
            'status': forms.Select(attrs={'placeholder': 'Select room status'}),
            'price_per_night': forms.NumberInput(attrs={'placeholder': 'Enter price per night'}),
            'size': forms.NumberInput(attrs={'placeholder': 'Enter room size in square meters'}),
        }
        
    amenities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter amenity name (e.g. Wi-Fi, Air Conditioner)'}),
            'description': forms.Textarea(attrs={'placeholder': 'Provide a description of the amenity'}),
        }
