# views.py
from django.shortcuts import render, get_object_or_404, redirect
from bookings.models import Booking, Payment
from bookings.forms import BookingForm, PaymentForm

def home(request):
    return render(request, 'base_generic.html')

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    payments = Payment.objects.filter(booking=booking)
    return render(request, 'booking_detail.html', {'booking': booking, 'payments': payments})

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_detail', pk=booking.pk)
        else:
            print(form.errors)  # เพิ่มการตรวจสอบข้อผิดพลาดของฟอร์ม
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})

def payment_create(request, booking_pk):
    booking = get_object_or_404(Booking, pk=booking_pk)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form, 'booking': booking})
