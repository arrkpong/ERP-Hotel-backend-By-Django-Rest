# rooms/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Amenity
from .forms import RoomForm, AmenityForm

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'room_detail.html', {'room': room})

def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'room_form.html', {'form': form})

def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_form.html', {'form': form})

def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        room.delete()
        return redirect('room_list')
    return render(request, 'room_confirm_delete.html', {'room': room})

def amenity_list(request):
    amenities = Amenity.objects.all()
    return render(request, 'amenity_list.html', {'amenities': amenities})

def amenity_detail(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    return render(request, 'amenity_detail.html', {'amenity': amenity})

def amenity_create(request):
    if request.method == "POST":
        form = AmenityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('amenity_list')
    else:
        form = AmenityForm()
    return render(request, 'amenity_form.html', {'form': form})

def amenity_edit(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == "POST":
        form = AmenityForm(request.POST, instance=amenity)
        if form.is_valid():
            form.save()
            return redirect('amenity_detail', pk=amenity.pk)
    else:
        form = AmenityForm(instance=amenity)
    return render(request, 'amenity_form.html', {'form': form})

def amenity_delete(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == "POST":
        amenity.delete()
        return redirect('amenity_list')
    return render(request, 'amenity_confirm_delete.html', {'amenity': amenity})
